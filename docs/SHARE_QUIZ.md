# Share / Inline Quiz Integration (Laado-Quiz-Bot)

This new integration adds an example module that provides "Share" and "Share interactive" buttons for quizzes
using python-telegram-bot v20+ and Telegram Inline Mode. It demonstrates how to:

- Show a quiz card with buttons:
  - Start private chat
  - Start in group
  - Share quiz (opens native forward/share sheet)
  - Share interactive (opens inline picker pre-filled for this bot)
- Respond to inline queries and return an interactive message (with Play button) that can be inserted into any chat.

Files added on branch `share-quiz-inline`:

- `telegram_share_quiz.py` — example implementation (no secrets included)
- `docs/SHARE_QUIZ.md` — integration & testing instructions

IMPORTANT: No secrets or BOT_TOKEN values were added to the repository. Set BOT_TOKEN as an environment variable in your deployment.

---

Integration instructions (quick):

1. Enable Inline Mode for your bot in BotFather (you mentioned it's already enabled for @comeback_009bot).
2. Add `telegram_share_quiz.py` to your project (or copy the helpers into your bot code).
3. Set BOT_TOKEN in the environment where the bot runs (e.g., export BOT_TOKEN="<your token>").
4. Import and register handlers or run the example as a standalone service:

   - To register in an existing Application/Dispatcher:
     - from telegram_share_quiz import build_application, get_share_keyboard
     - Either build a separate Application with `build_application()` or add the handlers from the module to your existing Application.

   - To send a quiz card from your existing flow:
     - Use `get_share_keyboard(quiz_id, quiz_title)` to obtain the InlineKeyboardMarkup and include it in your reply.

5. Test locally:
   - Run `python telegram_share_quiz.py` with BOT_TOKEN set.
   - Use `/quiz 12345 "My Sample Quiz"` to send a sample quiz card.
   - Tap "Share quiz" to open the native forward/share sheet.
   - Tap "Share interactive" to open the inline picker for @comeback_009bot; choose a chat and insert the interactive invite.
   - Tap "Play" in the destination chat to trigger the callback handler (replace the placeholder with your quiz-start logic).

Notes & limitations:

- Bots cannot silently send messages into arbitrary chats without user action. The inline flow requires the sharing user to choose an inline result; the inserted message is then posted to the target chat by Telegram on behalf of the user.
- `t.me/share/url` forwards a plain link/text. To add an interactive panel (buttons, Play), use the inline result (switch_inline_query + inline_query handler).

If you want me to replace or patch existing files in the repository (instead of adding a new module), tell me the exact file path and I will update it and open a pull request.
