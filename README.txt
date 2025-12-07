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
