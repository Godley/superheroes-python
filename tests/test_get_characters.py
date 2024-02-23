import pytest
from unittest.mock import MagicMock

from superheroes_python.get_characters import get_characters

def test_get_characters():
    result = get_characters()
    assert result


def test_response_failure(mocker):
    response = MagicMock()
    response.status_code = 400
    mocker.patch(
        "superheroes_python.get_characters.requests.get",
        return_value=response
    )
    with pytest.raises(Exception) as e:
        get_characters()
        assert str(e) == "Status code was 400"
