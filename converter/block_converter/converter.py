from .parser import SlackBlockParser


class SlackBlockConverter:

    @classmethod
    def convert(cls, data):
        parsed_data = SlackBlockParser().parse(data)
        if isinstance(parsed_data, list):
            return_data = []
            for item in parsed_data:
                return_data.append(cls._convert_block(item))
            return return_data
        else:
            return cls._convert_block(parsed_data)

    @classmethod
    def _convert_block(cls, data):
        if "class" in data:
            return cls._convert_class(data)
        return ""

    @classmethod
    def _convert_args(cls, args):
        return_value = ""
        for key, value in args.items():
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
                return_value += f"{key}={cls._convert_class(value)}"
            elif isinstance(value, list):
                if return_value:
                    return_value += ", "
                list_value = ''
                for item in value:
                    if list_value:
                        list_value += ", "
                    list_value += f"{cls._convert_class(item)}"
                return_value += f"{key}=[{list_value}]"
        return return_value

    @classmethod
    def _convert_class(cls, data):
        class_name = data["class"]
        args = ""
        if "args" in data:
            args = cls._convert_args(data["args"])

        return f"{class_name}({args})"
