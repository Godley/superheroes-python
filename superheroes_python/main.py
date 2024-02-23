from superheroes_python.get_characters import get_characters
from typing import Dict


def battle(hero_name: str, villain_name: str) -> Dict:
    characters = get_characters()

    hero: Dict = None
    villain: Dict = None

    if characters.get("items") is None:
        raise Exception("Invalid input structure")

    for character in characters["items"]:
        if character["name"] == hero_name and character["type"] == "hero":
            hero = character
        if character["name"] == villain_name and character["type"] == "villain":
            villain = character

    if hero.get("weakness") == villain_name:
        hero["score"] -= 1

    if hero is None or villain is None:
        raise Exception("Hero or villain name not found in input structure")

    return hero if hero["score"] >= villain["score"] else villain

if __name__ == "__main__":
    print(battle("Batman", "Joker"))