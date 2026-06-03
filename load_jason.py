import json
import os

def load_json(path):
    if not os.path.exists(path):
        return {}

    if os.path.getsize(path) == 0:
        return {}

    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")