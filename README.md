# Telegram Bot Template

Use this template for starting to create a new telegram bot.

## Features

- SQLAlchemy as ORM.
- Use in-memory database to start persisting right away.
- Load environment variables from .env files or from OS.
- Log events in file, stderr/stdout, and rotate log files.

## Startup

Create a virtual environment for the bot: 

`python -m venv /path/to/bot`

Activate the virtual environment:

- Windows:
  - Git Bash: `source /path/to/bot/Scripts/activate`
  - CMD: `Scripts\activate.bat`
  - PS: `.\path\to\bot\Scripts\Activate.ps1`
- *NIX POSIX: `. /path/to/bot/bin/activate`

Install dependencies: `pip install -r /path/to/bot/requirements.txt`

Start the bot: `python /pat/to/bot/src/__init__.py`

## TODO

- Add Payments API
- Organize ORM models and repositories