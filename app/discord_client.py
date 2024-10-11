from discord import Webhook, RequestsWebhookAdapter
import os

# Get the Discord webhook URL from environment variable
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
discord_webhook = Webhook.from_url(DISCORD_WEBHOOK_URL, adapter=RequestsWebhookAdapter())

def send_to_discord(content):
    try:
        discord_webhook.send(content)
        print("Message sent to discord", content)
    except Exception as e:
        print(f'Error sending to Discord: {e}')
