BLOCK_TYPE_MAPPER = {
    "mrkdwn": "MarkdownTextObject",
    "plain_text": "PlainTextObject",
    "section": "SectionBlock",
    "divider": "DividerBlock",
    "image": "ImageBlock",
    "actions": "ActionsBlock",
    "context": "ContextBlock",
    "input": "InputBlock",
    "file": "FileBlock",
    "call": "CallBlock",
    "header": "HeaderBlock",
    "button": "ButtonElement",
    "checkboxes": "CheckboxesElement",
    "datepicker": "DatePickerElement",
    "timepicker": "TimePickerElement",
    "image": "ImageElement",
    "static_select": "StaticSelectElement",
    "multi_static_select": "StaticMultiSelectElement",
    "static_select": "SelectElement",
    "external_select": "ExternalDataSelectElement",
    "multi_external_select": "ExternalDataMultiSelectElement",
    "users_select": "UserSelectElement",
    "multi_users_select": "UserMultiSelectElement",
    "conversations_select": "ConversationSelectElement",
    "multi_conversations_select": "ConversationMultiSelectElement",
    "channels_select": "ChannelSelectElement",
    "multi_channels_select": "ChannelMultiSelectElement",
    "plain_text_input": "PlainTextInputElement",
    "radio_buttons": "RadioButtonsElement",
    "overflow": "OverflowMenuElement",
    "option": "Option"
}

def get_slack_class(block_type):
    try:
        return BLOCK_TYPE_MAPPER[block_type]
    except KeyError:
        raise ValueError(f"The class for {block_type} is not defined.")
