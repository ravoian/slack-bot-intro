# Import used modules
import json

# Install requests with python -m pip install requests 
import requests

def post_message_custom():
    # Can be found under Bot User OAuth Token 
    bot_token: str = '<your_bot_token>'

    # Add authorization token in header due to odd behavior noted sometimes when passed as parameter for new Slack bots
    # Content-type not set to allow requests module to set it depending on the content, may need to be set for specific cases
    headers: dict = {
        'Authorization': f'Bearer {bot_token}',
    }

    # Use testing channel for this example
    params: dict = {
        'channel': '<my_test_channel_id>', 
        'text': 'Test',
        'username': 'CustomBot',
        'icon_emoji': ':customs:',
    }

    # Post the request and return the response as a pretty-printed json
    response: json = requests.post(url='https://slack.com/api/chat.postMessage', params=params, headers=headers).json()
    print(json.dumps(response, indent=2))


post_message_custom()
