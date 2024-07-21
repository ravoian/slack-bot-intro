# System modules
import json

# Install requests with python -m pip install requests 
import requests

def post_message_with_blocks():
    # Can be found under Bot User OAuth Token
    bot_token: str = '<your_token_here>'

    # Add authorization token in header due to odd behavior noted sometimes when passed as parameter for new Slack bots
    # Content-type not set to allow requests module to set it depending on the content, may need to be set for specific cases
    headers: dict = {
        'Authorization': f'Bearer {bot_token}',
        'Content-type': 'application/x-www-form-urlencoded'
    }

    # Create sample blocks using https://api.slack.com/tools/block-kit-builder
    blocks: list = [
        {
            "type": "image",
            "image_url": "https://i1.wp.com/thetempest.co/wp-content/uploads/2017/08/The-wise-words-of-Michael-Scott-Imgur-2.jpg?w=1024&ssl=1",
            "alt_text": "inspiration"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Pick an item from the dropdown list"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select an item",
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "*this is plain_text text*",
                        },
                        "value": "value-0"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "*this is plain_text text*",
                        },
                        "value": "value-1"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "*this is plain_text text*",
                        },
                        "value": "value-2"
                    }
                ],
                "action_id": "static_select-action"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "This is a section block with a button."
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Click Me",
                },
                "value": "click_me_123",
                "action_id": "button-action"
            }
        }
    ]

    # Use testing channel for this example
    params: dict = {
        'channel': '<my_test_channel_id>', 
        'text': 'Test',
        'blocks': json.dumps(blocks)
    }

    # Post the request and return the response as a pretty-printed json
    response: json = requests.post(url='https://slack.com/api/chat.postMessage', params=params, headers=headers).json()
    print(json.dumps(response, indent=2))


post_message_with_blocks()
