import os
import feedparser
import json

def check_environment_variables():
    # List of required environment variables
    required_env_vars = [
        'TELEGRAM_TOKEN',
        'CHAT_ID',
        'DISCORD_WEBHOOK_URL',
    ]

    for var in required_env_vars:
        value = os.getenv(var)
        if value:
            print(f"{var}: {value}")
        else:
            print(f"Warning: {var} is not set.")


def fetch_rss_feed(url, output_file='rss_feed.json'):
    feed = feedparser.parse(url)
    entries = feed.entries
    feed_data = [dict(entry) for entry in entries]
    
    with open(output_file, 'w') as json_file:
        json.dump(feed_data, json_file, indent=4)
    
    print(f"Saved RSS feed to {output_file}")
    return entries

if __name__ == '__main__':
    fetch_rss_feed('https://www.gadgets360.com/rss/feeds')
