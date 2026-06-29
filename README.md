# 🎯 Laado Quiz Bot

A feature-rich Telegram bot for creating and playing interactive quizzes with a beautiful Hindi/Hinglish interface!

## ✨ Features

- **📝 Create Custom Quizzes**: Users can create their own quizzes with multiple questions
- **🎮 Play Quizzes**: Interactive quiz playing experience with instant feedback
- **📊 Score Tracking**: Keep track of user scores and quiz statistics
- **💾 SQLite Database**: Persistent storage for quizzes and user data
- **🎨 Beautiful UI**: Hindi/Hinglish interface with emoji support
- **⚙️ Admin Control**: Owner-specific commands for bot statistics

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Telegram Bot Token (from BotFather)
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/manishakumarim7257/Laado-Quiz-Bot.git
cd Laado-Quiz-Bot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
cp sample.env .env
# Edit .env and add your BOT_TOKEN and OWNER_ID
```

4. **Run the bot**
```bash
python quiz_bot.py
```

## 📋 Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message |
| `/create` | Start creating a new quiz |
| `/play_id <quiz_id>` | Play a quiz by ID |
| `/cancel` | Cancel current operation |
| `/stats` | View bot statistics (Owner only) |

## 🎯 How to Use

### Creating a Quiz
1. Send `/create` command
2. Enter quiz title
3. Enter quiz description
4. Add questions one by one with:
   - Question text
   - Multiple options (2-4)
   - Correct answer
   - Explanation (optional)
5. Save the quiz and get a Quiz ID

### Playing a Quiz
1. Send `/play_id <quiz_id>` (get ID from creator)
2. Answer each question by tapping the buttons
3. View your final score

## 🛠️ Technology Stack

- **python-telegram-bot**: Telegram bot framework
- **SQLite3**: Database
- **python-dotenv**: Environment variable management

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## 📧 Support

For issues or questions, please open an issue on GitHub.

---

**Made with ❤️ by Manisha Kumari**
