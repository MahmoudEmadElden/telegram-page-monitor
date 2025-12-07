# Telegram Page Monitor Bot

This Python bot monitors a specific web page and sends a Telegram message whenever the page content changes. It is designed to notify the user immediately of any new updates.

## Features
- Monitors any web page URL for changes.
- Sends instant notifications via Telegram bot.
- Stores the last known page hash to detect updates.
- Configurable check interval (default: every 5 minutes).

## Requirements
- Python 3.x
- `requests` library

Install dependencies:

```bash
pip install requests
Setup
1-Clone this repository:

git clone https://github.com/MahmoudEmadElden/telegram-page-monitor.git
cd telegram-page-monitor


2-Edit monitor.py to add your Telegram bot token and chat ID:

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"


3-Optional configuration (change URL or check interval):

URL = "https://example.com"
# Check interval in seconds (default 300 = 5 minutes)
CHECK_INTERVAL = 300
Usage

Run the bot:

python monitor.py


The bot will start monitoring the page.

Sends a Telegram message when any changes are detected.
