from telegram import Bot
import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

telegram_bot = Bot(token=TELEGRAM_TOKEN)
print("TELEGRAM_TOKEN", TELEGRAM_TOKEN)

def send_to_telegram(content):
    try:
        telegram_bot.send_message(chat_id=CHAT_ID, text=content, parse_mode='MarkdownV2')
        print('Message sent to telegram ', content)
    except Exception as e:
        print(f'Error sending to Telegram: {e}')
