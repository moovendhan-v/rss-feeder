import requests

def subscribe_to_feed(feed_url, hub_url, callback_url):
    data = {
        'hub.mode': 'subscribe',
        'hub.topic': feed_url,          # The RSS feed URL you want to follow
        'hub.callback': callback_url,   # Your webhook URL
        'hub.verify': 'async'
    }

    response = requests.post(hub_url, data=data)

    if response.status_code == 202:
        print('Subscription request accepted.')
    else:
        print(f'Subscription failed: {response.status_code}')

if __name__ == '__main__':
    feed_url = 'https://www.news18.com/commonfeeds/v1/eng/rss/tech.xml'
    hub_url = 'https://example.com/websub-hub-url'
    callback_url = 'https://yourdomain.com/webhook'

    subscribe_to_feed(feed_url, hub_url, callback_url)
