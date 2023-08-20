# Somnolog Bot
## Functional
- Add dream, set it's type, description
- Clear your dream history, delete last dream (I imagine that you will use it to correct mistakes)
- See your history of dreams
- See statistic

## Setting Up
1. You need your own bot token, get it there: https://t.me/BotFather.
2. Make token.txt with only your bot token in the src folder.
3. Make config.py with info about your database. Fields: user, password, host, db_name.
4. Start the console in the main folder (SomnologBot) and start `python -m venv venv` (Windows) | `python3 -m venv venv` (Linux) to install virtual environment.
5. Install requirements to your virtual environment. Activate venv through `call venv/Scripts/activate` (Windows) | `source venv/bin/activate` (Linux). Use `pip install -r requirements.txt`.
6. to start use `start_w.bat` (Windows) | `bash ./start_l.sh` (Linux).

## Technology Stack
- MySQL is used for database.
- Aiogram is used for Bot.

## Database Structure
You can see my database structure here: https://drawsql.app/teams/jpeg-jackals/diagrams/dreams.
