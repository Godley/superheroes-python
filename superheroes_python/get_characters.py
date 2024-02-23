import enum
import logging
from typing import Optional, List

import requests
from pydantic import BaseModel, ConfigDict, ValidationError, Json


CHARACTERS_URL = "https://s3.eu-west-2.amazonaws.com/build-circle/characters.json"


logger = logging.getLogger(__name__)


class CharacterType(enum.Enum):
    VILLAIN = "villain"
    HERO = "hero"


class Character(BaseModel):
    name: str
    score: float
    type: CharacterType
    weakness: Optional[str] = ""


class CharacterList(BaseModel):
    model_config = ConfigDict(strict=True)
    items: List[Character]

def get_characters() -> Optional[List]:
    result = requests.get(CHARACTERS_URL)
    if result.status_code != 200:
        raise Exception(f"Status code was {result.status_code}")
    try:
        result = CharacterList(**result.json())
    except ValidationError as e:
        logger.error(e)
        return None
    return result.items
