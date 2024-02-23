import requests
import json
from typing import Dict

CHARACTERS_URL = "https://s3.eu-west-2.amazonaws.com/build-circle/characters.json"

def get_characters() -> Dict:
    """
    1. Download from a given url
    2. load it into a dictionary for now
    3. return it
    :return:
    """
    result = requests.get(CHARACTERS_URL)
    if result.status_code != 200:
        raise Exception(f"Status code was {result.status_code}")
    loaded_result = json.loads(result.text)
    return loaded_result
