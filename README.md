# Somnolog bot

## Folder structure
- src for sources (scripts, token)
- db for database (MySQL)

## Functional
- Add dream, set it's type, description
- See your history of dreams
- See statistic
- Set notifications, bot will ask you about the dream at a certain time, so you won't forget to add dream

## Usage
1. You need your own bot token, get it there: https://t.me/BotFather.
2. Make token.txt with only your bot token in the src folder.
3. Start the console in the main folder (SomnologBot) and start `python -m venv venv` (Windows) | `python3 -m venv venv` (Linux) to install virtual environment.
4. Install aiogram to your virtual environment.
5. Windows: start the start_w.bat | Linux: start the start_l.sh.