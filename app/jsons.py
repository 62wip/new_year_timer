from json import load, dump, decoder

from config import JSON_FILE_NAME

def load_data() -> dict:
    try:
        with open(JSON_FILE_NAME, 'r') as file:
            return load(file)
    except (FileNotFoundError, decoder.JSONDecodeError):
        return {}

def dump_data(data: dict) -> None:
    with open(JSON_FILE_NAME, 'w') as file:
        dump(data, file, indent=2)