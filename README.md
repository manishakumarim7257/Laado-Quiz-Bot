# 🎯 Laado Quiz Bot

A powerful Telegram bot for creating and conducting interactive quizzes with group gameplay, real-time scoring, and leaderboards.

## ✨ Features

- **Create Custom Quizzes** - Build quizzes with multiple questions and options
- **Group Quiz Mode** - Play quizzes with friends in group chats
- **Real-time Leaderboard** - Live scoring with top 20 rankings
- **Quiz Customization** - Set titles, descriptions, timer, and add explanations
- **Share Quizzes** - Generate shareable links for your quizzes
- **Quiz Editing** - Edit quiz details after creation
- **Instant Feedback** - Get immediate explanations for answers

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- SQLite3

### Installation

```bash
git clone https://github.com/manishakumarim7257/Laado-Quiz-Bot.git
cd Laado-Quiz-Bot
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token_here
OWNER_ID=your_telegram_user_id_here
```

### Running the Bot

```bash
python quiz_bot.py
```

## 📖 Usage Guide

### Commands

- `/start` - Start the bot and see welcome message
- `/newquiz` - Create a new quiz
- `/skip` - Skip optional fields (description)
- `/undo` - Remove the last question
- `/done` - Finish quiz creation
- `/cancel` - Cancel quiz creation

### Creating a Quiz

1. Send `/newquiz`
2. Enter quiz title
3. (Optional) Add description or `/skip`
4. Click "Create a Question" button
5. Send quiz-mode polls (enable quiz mode when creating poll in Telegram)
6. Set time limit (15s, 30s, 1min, 2min)
7. Share or start the quiz

### Playing in Groups

1. Generate group link or forward the sharing link
2. Friends click "Join Quiz ➕"
3. Need minimum 2 users to start
4. Click "Start Quiz 🚀" when ready
5. Answer each question within the timer
6. View final leaderboard with rankings

## 📊 Database Schema

### Tables

**quizzes**
- quiz_id (Primary Key)
- creator_id
- title
- description
- timer (in seconds)

**questions**
- id (Primary Key)
- quiz_id (Foreign Key)
- question_text
- options (JSON array)
- correct_answer
- explanation
- pre_message

## 🔧 Technical Details

- **Framework**: python-telegram-bot
- **Database**: SQLite3
- **Architecture**: Conversation Handler pattern
- **Polling**: Telegram native polls with quiz mode
- **Score Tracking**: Real-time scoring with response time calculation

## 📝 Known Issues & TODOs

- [ ] Fix URL construction in share links
- [ ] Refactor nested function definitions
- [ ] Add quiz deletion feature
- [ ] Add user statistics tracking
- [ ] Add question analytics

## 🤝 Contributing

Feel free to fork and submit pull requests for improvements!

## 📄 License

This project is open source and available under the MIT License.

## 💬 Support

For issues or questions, please open a GitHub issue.

---

**Made with ❤️ by Manisha Kumar**
