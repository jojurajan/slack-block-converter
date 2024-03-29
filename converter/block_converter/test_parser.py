import pytest

from .parser import SlackBlockParser

@pytest.mark.parametrize(
    "data, expected_data",
    [
        (
            {
                "type":"section",
                "block_id":"title",
                "text":{
                    "type":"mrkdwn",
                    "text":"random_text_1",
                    "verbatim": False
                }
            },
            {
                "class": "SectionBlock",
                "args": {
                    "block_id": "title",
                    "text": {
                        "class": "MarkdownTextObject",
                        "args": {
                            "text": "random_text_1",
                            "verbatim": False
                        }
                    }
                }
            }
        ),
        (
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "This is a plain text section block.",
                    "emoji": True
                }
            },
            {'class': 'SectionBlock', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': 'This is a plain text section block.', 'emoji': True}}}}
        ),
        (
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This is a mrkdwn section block :ghost: *this is bold*, and ~this is crossed out~, and <https://google.com|this is a link>"
                }
            },
            {'class': 'SectionBlock', 'args': {'text': {'class': 'MarkdownTextObject', 'args': {'text': 'This is a mrkdwn section block :ghost: *this is bold*, and ~this is crossed out~, and <https://google.com|this is a link>'}}}}
        ),
        (
            {
                "type": "section",
                "fields": [
                    {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                        "emoji": True
                    },
                    {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                        "emoji": True
                    },
                    {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                        "emoji": True
                    },
                    {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                        "emoji": True
                    },
                    {
                        "type": "plain_text",
                        "text": "*this is plain_text text*",
                        "emoji": True
                    }
                ]
            },
            {'class': 'SectionBlock', 'args': {'fields': [{'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}]}}
        ),
        (
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Test block with users select"
                },
                "accessory": {
                    "type": "users_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a user",
                        "emoji": True
                    },
                    "action_id": "users_select-action"
                }
            },
            {'class': 'SectionBlock', 'args': {'text': {'class': 'MarkdownTextObject', 'args': {'text': 'Test block with users select'}}, 'accessory': {'class': 'UserSelectElement', 'args': {'placeholder': {'class': 'PlainTextObject', 'args': {'text': 'Select a user', 'emoji': True}}, 'action_id': 'users_select-action'}}}}
        ),
        (
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
                        "emoji": True
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": True
                            },
                            "value": "value-0"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": True
                            },
                            "value": "value-1"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": True
                            },
                            "value": "value-2"
                        }
                    ],
                    "action_id": "static_select-action"
                },
            },
            {'class': 'SectionBlock', 'args': {'text': {'class': 'MarkdownTextObject', 'args': {'text': 'Pick an item from the dropdown list'}}, 'accessory': {'class': 'SelectElement', 'args': {'placeholder': {'class': 'PlainTextObject', 'args': {'text': 'Select an item', 'emoji': True}}, 'options': [{'class': 'Option', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, 'value': 'value-0'}}, {'class': 'Option', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, 'value': 'value-1'}}, {'class': 'Option', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, 'value': 'value-2'}}], 'action_id': 'static_select-action'}}}}
        ),
        (
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Test block with multi conversations select"
                },
                "accessory": {
                    "type": "multi_conversations_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select conversations",
                        "emoji": True
                    },
                    "action_id": "multi_conversations_select-action"
                }
            },
            {'class': 'SectionBlock', 'args': {'text': {'class': 'MarkdownTextObject', 'args': {'text': 'Test block with multi conversations select'}}, 'accessory': {'class': 'ConversationMultiSelectElement', 'args': {'placeholder': {'class': 'PlainTextObject', 'args': {'text': 'Select conversations', 'emoji': True}}, 'action_id': 'multi_conversations_select-action'}}}}
        ),
        (
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
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "button-action"
                }
            },
            {'class': 'SectionBlock', 'args': {'text': {'class': 'MarkdownTextObject', 'args': {'text': 'This is a section block with a button.'}}, 'accessory': {'class': 'ButtonElement', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': 'Click Me', 'emoji': True}}, 'value': 'click_me_123', 'action_id': 'button-action'}}}}
        ),
        (
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
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "url": "https://google.com",
                    "action_id": "button-action"
                }
            },
            {'class': 'SectionBlock', 'args': {'text': {'class': 'MarkdownTextObject', 'args': {'text': 'This is a section block with a button.'}}, 'accessory': {'class': 'ButtonElement', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': 'Click Me', 'emoji': True}}, 'value': 'click_me_123', 'url': 'https://google.com', 'action_id': 'button-action'}}}}
        ),
        (
             {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This is a section block with an accessory image."
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://pbs.twimg.com/profile_images/625633822235693056/lNGUneLX_400x400.jpg",
                    "alt_text": "cute cat"
                }
            },
            {'class': 'SectionBlock', 'args': {'text': {'class': 'MarkdownTextObject', 'args': {'text': 'This is a section block with an accessory image.'}}, 'accessory': {'class': 'ImageElement', 'args': {'image_url': 'https://pbs.twimg.com/profile_images/625633822235693056/lNGUneLX_400x400.jpg', 'alt_text': 'cute cat'}}}}
        ),
        (
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This is a section block with an overflow menu."
                },
                "accessory": {
                    "type": "overflow",
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": True
                            },
                            "value": "value-0"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": True
                            },
                            "value": "value-1"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": True
                            },
                            "value": "value-2"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": True
                            },
                            "value": "value-3"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "*this is plain_text text*",
                                "emoji": True
                            },
                            "value": "value-4"
                        }
                    ],
                    "action_id": "overflow-action"
                }
            },
            {'class': 'SectionBlock', 'args': {'text': {'class': 'MarkdownTextObject', 'args': {'text': 'This is a section block with an overflow menu.'}}, 'accessory': {'class': 'OverflowMenuElement', 'args': {'options': [{'class': 'Option', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, 'value': 'value-0'}}, {'class': 'Option', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, 'value': 'value-1'}}, {'class': 'Option', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, 'value': 'value-2'}}, {'class': 'Option', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, 'value': 'value-3'}}, {'class': 'Option', 'args': {'text': {'class': 'PlainTextObject', 'args': {'text': '*this is plain_text text*', 'emoji': True}}, 'value': 'value-4'}}], 'action_id': 'overflow-action'}}}}
        ),
        (
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Pick a date for the deadline."
                },
                "accessory": {
                    "type": "datepicker",
                    "initial_date": "1990-04-28",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a date",
                        "emoji": True
                    },
                    "action_id": "datepicker-action"
                }
            },
            {'class': 'SectionBlock', 'args': {'text': {'class': 'MarkdownTextObject', 'args': {'text': 'Pick a date for the deadline.'}}, 'accessory': {'class': 'DatePickerElement', 'args': {'initial_date': '1990-04-28', 'placeholder': {'class': 'PlainTextObject', 'args': {'text': 'Select a date', 'emoji': True}}, 'action_id': 'datepicker-action'}}}}
        )
    ]
)
def test_block_parser(data, expected_data):
    slack_parser = SlackBlockParser()

    parsed_data = slack_parser.parse(data)
    assert expected_data == parsed_data
