import pytest

from .converter import SlackBlockConverter


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
            'SectionBlock(block_id="title", text=MarkdownTextObject(text="random_text_1", verbatim=False))'
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
            'SectionBlock(text=PlainTextObject(text="This is a plain text section block.", emoji=True))'
        ),
        (
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This is a mrkdwn section block :ghost: *this is bold*, and ~this is crossed out~, and <https://google.com|this is a link>"
                }
            },
            'SectionBlock(text=MarkdownTextObject(text="This is a mrkdwn section block :ghost: *this is bold*, and ~this is crossed out~, and <https://google.com|this is a link>"))'
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
            'SectionBlock(fields=[PlainTextObject(text="*this is plain_text text*", emoji=True), PlainTextObject(text="*this is plain_text text*", emoji=True), PlainTextObject(text="*this is plain_text text*", emoji=True), PlainTextObject(text="*this is plain_text text*", emoji=True), PlainTextObject(text="*this is plain_text text*", emoji=True)])'
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
            'SectionBlock(text=MarkdownTextObject(text="Test block with users select"), accessory=UserSelectElement(placeholder=PlainTextObject(text="Select a user", emoji=True), action_id="users_select-action"))'
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
            'SectionBlock(text=MarkdownTextObject(text="Pick an item from the dropdown list"), accessory=SelectElement(placeholder=PlainTextObject(text="Select an item", emoji=True), options=[Option(text=PlainTextObject(text="*this is plain_text text*", emoji=True), value="value-0"), Option(text=PlainTextObject(text="*this is plain_text text*", emoji=True), value="value-1"), Option(text=PlainTextObject(text="*this is plain_text text*", emoji=True), value="value-2")], action_id="static_select-action"))'
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
            'SectionBlock(text=MarkdownTextObject(text="Test block with multi conversations select"), accessory=ConversationMultiSelectElement(placeholder=PlainTextObject(text="Select conversations", emoji=True), action_id="multi_conversations_select-action"))'
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
            'SectionBlock(text=MarkdownTextObject(text="This is a section block with a button."), accessory=ButtonElement(text=PlainTextObject(text="Click Me", emoji=True), value="click_me_123", action_id="button-action"))'
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
            'SectionBlock(text=MarkdownTextObject(text="This is a section block with a button."), accessory=ButtonElement(text=PlainTextObject(text="Click Me", emoji=True), value="click_me_123", url="https://google.com", action_id="button-action"))'
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
            'SectionBlock(text=MarkdownTextObject(text="This is a section block with an accessory image."), accessory=ImageElement(image_url="https://pbs.twimg.com/profile_images/625633822235693056/lNGUneLX_400x400.jpg", alt_text="cute cat"))'
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
            'SectionBlock(text=MarkdownTextObject(text="This is a section block with an overflow menu."), accessory=OverflowMenuElement(options=[Option(text=PlainTextObject(text="*this is plain_text text*", emoji=True), value="value-0"), Option(text=PlainTextObject(text="*this is plain_text text*", emoji=True), value="value-1"), Option(text=PlainTextObject(text="*this is plain_text text*", emoji=True), value="value-2"), Option(text=PlainTextObject(text="*this is plain_text text*", emoji=True), value="value-3"), Option(text=PlainTextObject(text="*this is plain_text text*", emoji=True), value="value-4")], action_id="overflow-action"))'
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
            'SectionBlock(text=MarkdownTextObject(text="Pick a date for the deadline."), accessory=DatePickerElement(initial_date="1990-04-28", placeholder=PlainTextObject(text="Select a date", emoji=True), action_id="datepicker-action"))'
        )
    ]
)
def test_block_converter(data, expected_data):
    slack_converter = SlackBlockConverter()

    converted_data = slack_converter.convert(data)
    assert expected_data == converted_data
