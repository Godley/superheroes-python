from superheroes_python.get_characters import get_characters, CharacterType, Character
from typing import Optional


def battle(hero_name: str, villain_name: str) -> Character:
    characters = get_characters()

    hero: Optional[Character] = None
    villain: Optional[Character] = None

    if characters is None:
        raise Exception("Invalid input structure")

    for character in characters:
        if character.name == hero_name and character.type.value == CharacterType.HERO.value:
            hero = character
        if character.name == villain_name and character.type.value == CharacterType.VILLAIN.value:
            villain = character

    if hero.weakness == villain_name:
        hero.score -= 1

    if hero is None or villain is None:
        raise Exception("Hero or villain name not found in input structure")

    return hero if hero.score >= villain.score else villain

if __name__ == "__main__":
    print(battle("Batman", "Joker"))