# Post interview install notes
In order to get the tests working, I:
- completely wiped and reinstalled my OS (this was overdue anyway!)
- Installed python 3.9 using `brew install python@3.9`
  - I found installing python 3.12 caused the same issues exhibited during the interview, so went with the lowest possible version mentioned in the instructions.
- ran virtualenv using `brew install virtualenv`, then `python3.9 -m virtualenv .venv` within the directory
- ran poetry install using `pip install poetry`, `poetry install`
- tests now running successfully using `poetry run pytest`