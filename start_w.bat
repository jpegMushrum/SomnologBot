@echo off

call %~dp0/venv/Scripts/activate

cd src

python bot.py

pause