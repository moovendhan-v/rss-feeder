import json
import feedparser
from app.db import initialize_db, store_sent_link, has_been_sent
from app.telegram_client import send_to_telegram
from app.discord_client import send_to_discord
import time
from datetime import datetime, timedelta, timezone

# Time interval in seconds
time_to_sleep = 5

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    return feed.entries

def store_sent_links(entries):
    for entry in entries:
        link = entry.link
        if not has_been_sent(link):
            store_sent_link(link)

def check_all_rss_feeds(feeds):
    # Get the current time in UTC with timezone awareness
    current_time = datetime.now(timezone.utc)
    cutoff_time = current_time - timedelta(hours=1)

    for feed_url in feeds:
        entries = fetch_rss_feed(feed_url)

        recent_entries = []

        for entry in entries:
            entry_time = datetime.fromtimestamp(time.mktime(entry.published_parsed), timezone.utc)
            if entry_time > cutoff_time and not has_been_sent(entry.link):
                recent_entries.append(entry)

        if not recent_entries:
            print(f"No new entries found for {feed_url} ")
            continue

        print(f"Fetching new entries from {feed_url} ..")

        # Store new entries in the database
        store_sent_links(recent_entries)

        # Send notifications for recent entries
        for entry in recent_entries:
            link = entry.link
            title = entry.title
            
            content = f"New post: {title}\n{link}"
            send_to_telegram(content)  # Send to Telegram
            send_to_discord(content)    # Send to Discord
            time.sleep(time_to_sleep)    # Wait for timeToSleep seconds before the next message

def load_feeds_from_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config.get('feeds', [])

if __name__ == '__main__':
    initialize_db()

    # Load feeds from config.json
    feeds = load_feeds_from_config()

    while True:  # Infinite loop to keep checking feeds
        check_all_rss_feeds(feeds)
        time.sleep(time_to_sleep)  # Wait for the defined interval before the next check
