import json


def load_default_headers():
    """
    Load default headers from conf_file
    """

    return {
      "cache-control": "no-cache; no-store; max-age = 0"
    }
