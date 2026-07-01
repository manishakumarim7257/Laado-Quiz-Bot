# Add Share / Share interactive buttons + inline-mode flow for quizzes

This PR adds an example module and documentation to provide interactive sharing features for quizzes.

Changes:
- Add `telegram_share_quiz.py` — example implementation (python-telegram-bot v20+)
- Add `docs/SHARE_QUIZ.md` — integration & testing instructions

How to test:
1. Set BOT_TOKEN in environment
2. Run the example or register handlers in your bot
3. Use /quiz to send a sample quiz card and test the Share/Share interactive flows
