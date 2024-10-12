from discord import Webhook, RequestsWebhookAdapter
import os
from discord import Embed

# Get the Discord webhook URL from environment variable
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
discord_webhook = Webhook.from_url(DISCORD_WEBHOOK_URL, adapter=RequestsWebhookAdapter())

def send_to_discord(content):
    try:
        discord_webhook.send(content)
        print("Message sent to discord", content)
    except Exception as e:
        print(f'Error sending to Discord: {e}')

def discord_message_embed(entry):
    """Format the message for Discord as an embed"""
    link = entry.link
    title = entry.title
    published = entry.published
    summary = entry.summary if 'summary' in entry else "No summary available"

    # Extract an image URL if available in the entry
    image_url = None
    if 'media_content' in entry:
        image_url = entry.media_content[0]['url']  # Usually, images are stored in the media_content field

    # Create a Discord Embed object
    embed = Embed(
        title=title, 
        description=summary, 
        url=link, 
        color=0x00ff00  # Green color
    )
    
    # Add additional fields to the embed
    embed.add_field(name="Published", value=published, inline=True)
    embed.add_field(name="Link", value=link, inline=True)

    # If an image URL is available, add the image to the embed
    if image_url:
        embed.set_image(url=image_url)

    return embed
