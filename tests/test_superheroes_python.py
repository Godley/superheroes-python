from superheroes_python.main import battle
from superheroes_python.get_characters import CharacterList, Character
import pytest


def test_battle_returns_the_hero_if_they_have_a_higher_score(mocker):
    mocker.patch(
        "superheroes_python.main.get_characters",
        return_value=[Character(name="Winner", score=9.0, type="hero"),
                      Character(name="Loser", score=8.0, type="villain")]
    )

    assert battle("Winner", "Loser") == Character(name="Winner", score=9.0, type="hero")

def test_battle_raises_if_character_not_found(mocker):
    mocker.patch(
        "superheroes_python.main.get_characters",
        return_value=[Character(name="Winner", score=9.0, type="hero"),
                                          Character(name="Loser", score=8.0, type="villain")])

    with pytest.raises(Exception) as e_info:
        battle("Not_Found", "Loser")
        assert str(e_info) == "Hero or villain name not found in input structure"


def test_weakness_reduces_score(mocker):
    mocker.patch(
        "superheroes_python.main.get_characters",
        return_value=[Character(name="Winner", score=10.0, type="hero", weakness="Loser"),
                      Character(name="Loser", score=8.0, type="villain")])

    assert battle("Winner", "Loser").score == 9.0


def test_hero_name_in_villain_slot(mocker):
    mocker.patch(
        "superheroes_python.main.get_characters",
        return_value=[Character(name="Winner", score=9.0, type="hero"),
                                          Character(name="Loser", score=8.0, type="villain")])

    with pytest.raises(Exception) as e_info:
        battle("Loser", "Winner")
        assert str(e_info) == "Hero or villain name not found in input structure"


def test_bad_input(mocker):
    mocker.patch(
        "superheroes_python.main.get_characters",
        return_value=[Character(name="Winner", score=9.0, type="hero"),
                                          Character(name="Loser", score=8.0, type="villain")])

    with pytest.raises(Exception) as e_info:
        battle("Loser", "Winner")
        assert str(e_info) == "Invalid input structure"

