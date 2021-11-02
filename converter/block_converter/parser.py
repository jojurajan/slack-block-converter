
class SlackBlockParser:
    non_changing_keys = ["action_id", "block_id", "value", "url", "image_url", "alt_text", "initial_date"]

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
            "option": "Option"
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

    def convert(self, data):
        if isinstance(data, list):
            return_data = []
            for item in data:
                return_data.append(self._convert_block(item))
            return return_data
        else:
            return self._convert_block(data)

    def _convert_block(self, data):
        if "class" in data:
            return self._convert_class(data)
        return ""

    def _convert_args(self, args):
        return_value = ""
        for key, value in args.items():
            print(key, value)
            if isinstance(value, str):
                if return_value:
                    return_value += ", "
                return_value += f'{key}="{value}"'
            elif isinstance(value, bool):
                if return_value:
                    return_value += ", "
                return_value += f'{key}={value}'
            elif isinstance(value, dict):
                if return_value:
                    return_value += ", "
                return_value += f"{key}={self._convert_class(value)}"
            elif isinstance(value, list):
                if return_value:
                    return_value += ", "
                list_value = ''
                for item in value:
                    if list_value:
                        list_value += ", "
                    list_value += f"{self._convert_class(item)}"
                return_value += f"{key}=[{list_value}]"
        return return_value

    def _convert_class(self, data):
        class_name = data["class"]
        args = ""
        if "args" in data:
            args = self._convert_args(data["args"])

        return f"{class_name}({args})"
