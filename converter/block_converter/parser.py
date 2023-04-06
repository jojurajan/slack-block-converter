
class SlackBlockParser:
    non_changing_keys = [
        "action_id", "block_id", "value", "url", "image_url", "alt_text",
        "initial_date", "initial_time", "initial_conversation", "initial_user",
        "initial_channel"]

    def parse(self, data):
        if isinstance(data, list):
            return [self._parse_block(block) for block in data]
        elif isinstance(data, dict):
            return self._parse_block(data)
        return parsed_data

    def _parse_block(self, data):
        return_data = {
            "class": self._get_class(data.pop("type")),
            "args": {}
        }
        for key, value in data.items():
            if key in self.non_changing_keys:
                return_data["args"][key] = value
                continue
            return_data["args"][key] = getattr(self, f"_parse_{key}")(value)
        return return_data

    def _get_type(self, data):
        return data.get("type")


    def _get_class(self, block_type):
        mapper = {
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
            "option": "Option",
            "filter": "ConversationFilter"
        }
        try:
            return mapper[block_type]
        except KeyError:
            raise ValueError("Invalid block_type provided.")

    def _parse_text(self, data):
        return_data = {
            "class": self._get_class(data.pop("type"))
        }
        return_data.update({
            "args": data
        })
        return return_data

    def _parse_section(self, data):
        return_data = {
            "class": self._get_class(data.pop("type")),
            "args": {}
        }
        for key, value in data.items():
            if key in self.non_changing_keys:
                return_data["args"][key] = value
                continue
            return_data["args"][key] = getattr(self, f"_parse_{key}")(value)
        return return_data

    def _parse_fields(self, data):
        return_data = []
        for item in data:
            block_type = self._get_type(item)
            if block_type in ["plain_text", "mrkdwn"]:
                return_data.append(self._parse_text(item))
        return return_data

    def _parse_options(self, data):
        return_data = []
        for item in data:
            return_data.append(self._parse_option(item))
        return return_data

    def _parse_option(self, data):
        return_data = {
            "class": self._get_class("option"),
            "args": {}
        }
        for key, value in data.items():
            if key == "value":
                return_data["args"][key] = value
                continue
            return_data["args"][key] = getattr(self, f"_parse_{key}")(value)
        return return_data

    def _parse_accessory(self, data):
        return_data = {
            "class": self._get_class(data.pop("type")),
            "args": {}
        }
        for key, value in data.items():
            if key in self.non_changing_keys:
                return_data["args"][key] = value
                continue
            return_data["args"][key] = getattr(self, f"_parse_{key}")(value)
        return return_data

    def _parse_placeholder(self, data):
        return self._parse_text(data)

    def _parse_description(self, data):
        return self._parse_text(data)

    def _parse_title(self, data):
        return self._parse_text(data)

    def _parse_elements(self, data):
        return_data = []
        for item in data:
            block_type = self._get_type(item)
            if block_type in ["plain_text", "mrkdwn"]:
                return_data.append(self._parse_text(item))
            else:
                return_data.append(self.parse(item))
        return return_data

    def _parse_filter(self, data):
        return_data = {
            "class": self._get_class("filter"),
            "args": {}
        }
        for key, value in data.items():
            if key in ["value", "include"]:
                return_data["args"][key] = value
                continue
            return_data["args"][key] = getattr(self, f"_parse_{key}")(value)
        return return_data

    def _parse_dispatch_action(self, data):
        return bool(data)

    def _parse_element(self, data):
        return_data = {
            "class": self._get_class(data.pop("type"))
        }
        return_data.update({
            "args": data
        })
        return return_data

    def _parse_label(self, data):
        return self._parse_text(data)
