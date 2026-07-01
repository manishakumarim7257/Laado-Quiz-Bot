"""
telegram_share_quiz.py

Add-on module for Laado-Quiz-Bot: provides an example implementation (python-telegram-bot v20+)
that adds "Start private chat", "Start in group", "Share quiz" (native share sheet), and
"Share interactive" (inline-mode prefilled query) buttons and an inline query handler.

Usage: import the helpers and handlers into your existing bot project or run this file
as a standalone example after setting BOT_TOKEN in your environment.

IMPORTANT: This file does NOT include any secrets. Set BOT_TOKEN as an environment
variable before running.
"""

import logging
from uuid import uuid4
from urllib.parse import quote
import os

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    InlineQueryHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CONFIG - read BOT_TOKEN from environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = "comeback_009bot"  # your bot's username (without @)

if not BOT_TOKEN:
    logger.warning("BOT_TOKEN not set in environment. Set BOT_TOKEN before running this file.")

# Utility: build share/start keyboard for a quiz
def get_share_keyboard(quiz_id: str, quiz_title: str = "Quiz") -> InlineKeyboardMarkup:
    """
    Returns an InlineKeyboardMarkup with:
      - Start private chat
      - Start in group
      - Share quiz (opens native forward/share sheet)
      - Share interactive (switch_inline_query to open inline picker)
    Use this keyboard when sending your quiz card in chats.
    """
    quiz_url = f"https://your.site/quiz/{quiz_id}"  # optional landing page
    share_text = f"Play this quiz: {quiz_title}\n{quiz_url}"

    keyboard = [
        [
            InlineKeyboardButton(
                text="Start private chat",
                url=f"https://t.me/{BOT_USERNAME}?start=quiz_{quiz_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="Start in group",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            # Opens Telegram share dialog / forward sheet (plain link + text)
            InlineKeyboardButton(
                text="Share quiz",
                url=f"https://t.me/share/url?url={quote(quiz_url)}&text={quote(share_text)}",
            ),
            # Opens inline query UI for this bot with a pre-filled query
            InlineKeyboardButton(
                text="Share interactive",
                switch_inline_query=f"quiz:{quiz_id}",
            ),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


# Example: send quiz card in a chat (replace your old send function with this)
async def send_quiz_card(update: Update, context: ContextTypes.DEFAULT_TYPE, quiz_id: str, quiz_title: str):
    text = f"🎯 {quiz_title}\nTap a button to share or start."
    keyboard = get_share_keyboard(quiz_id, quiz_title)
    # If invoked from command, update.message exists; otherwise use context.bot.send_message
    if update.message:
        await update.message.reply_text(text, reply_markup=keyboard)
    else:
        # used for other flows
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=keyboard)


# Handlers
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start and parse payloads like start=quiz_<id>"""
    args = context.args
    text = "Welcome! Use the quiz buttons to share or start a quiz."
    if args:
        payload = args[0]
        if payload.startswith("quiz_"):
            quiz_id = payload.split("_", 1)[1]
            # Customize behavior: show quiz intro or directly start
            text = f"You opened the bot for quiz {quiz_id}. Tap Play to begin."
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("Play", callback_data=f"play:{quiz_id}")]]
            )
            await update.message.reply_text(text, reply_markup=keyboard)
            return
    await update.message.reply_text(text)


async def make_quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Example command to send a quiz card.
    Usage: /quiz <quiz_id> <optional title>
    e.g. /quiz 12345 "My Quiz"
    """
    if not context.args:
        await update.message.reply_text("Usage: /quiz <quiz_id> [title]")
        return
    quiz_id = context.args[0]
    quiz_title = " ".join(context.args[1:]) if len(context.args) > 1 else f"Quiz {quiz_id}"
    await send_quiz_card(update, context, quiz_id, quiz_title)


async def inline_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Respond to inline queries. We expect switch_inline_query to send "quiz:<quiz_id>"
    The result will be an article whose inserted message includes an interactive Play button.
    """
    query = update.inline_query.query or ""
    # default fallback if user opens inline picker without prefilled query
    quiz_id = None
    if query.startswith("quiz:"):
        quiz_id = query.split(":", 1)[1].strip()
    else:
        # Optionally, you can attempt to parse natural queries or return a list of popular quizzes
        # For now return empty list if no quiz_id provided
        await update.inline_query.answer([], cache_time=0)
        return

    quiz_title = f"Quiz {quiz_id}"  # fetch title from DB if available

    text = f"🎲 Invitation: {quiz_title}\nTap Play to start the quiz."
    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Play", callback_data=f"play:{quiz_id}")]]
    )

    result = InlineQueryResultArticle(
        id=str(uuid4()),
        title=f"Invite players to: {quiz_title}",
        input_message_content=InputTextMessageContent(text),
        reply_markup=buttons,
    )
    await update.inline_query.answer(results=[result], cache_time=0)


async def callback_play_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle callback when a user taps "Play" in the inserted interactive panel.
    This could start the quiz flow (send first question as poll, or start a game, etc.)
    For demo: sends a confirmation message.
    """
    query = update.callback_query
    await query.answer()  # acknowledge callback to remove loading indicator
    data = query.data or ""
    if data.startswith("play:"):
        quiz_id = data.split(":", 1)[1]
        # TODO: integrate with your quiz engine — send quiz questions, etc.
        await query.message.reply_text(f"▶️ Starting quiz {quiz_id} for this chat...")
    else:
        await query.message.reply_text("Unknown action.")


async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I didn't understand that command. Use /quiz <id> to send a quiz card.")


def build_application(token: str = None):
    token = token or BOT_TOKEN
    if not token:
        raise RuntimeError("BOT_TOKEN is required to build the application. Set BOT_TOKEN in env or pass token param.")
    app = ApplicationBuilder().token(token).build()

    # Commands
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("quiz", make_quiz_command))

    # Inline query handler (must be enabled in BotFather)
    app.add_handler(InlineQueryHandler(inline_query_handler))

    # Callback handler for Play (and other callback_data patterns)
    app.add_handler(CallbackQueryHandler(callback_play_handler, pattern=r"^play:"))

    # Fallback
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))

    return app


def main():
    app = build_application()
    logger.info("Starting Laado-Quiz-Bot example (share/inline) application...")
    app.run_polling()


if __name__ == "__main__":
    main()
