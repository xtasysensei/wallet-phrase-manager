# Seed phrase manager
This is a project primarily written in **python**.
It aims to help users manage their wallet seed phrases. The Phrases are hashed and stored in a _json_ file which can be unhashed and retrieved at any time. Since it is purely offline, users can manage the _json_ file themselves by making multiple backup(both remote and local). Creating and managing it in a git repo is a very viable method.

## Requirements
- python(version >=3)
- [python poetry](https://python-poetry.org/)
- Terminal emulator
It is written to be cross-platform so it works on Windows, MacOS, Linux, FreeBSD and even a Potato.

## Usage
Open a shell, and run:
```bash
git clone git@github.com:xtasysensei/wallet-phrase-manager.git
cd wallet-phrase-manager
poetry install
poetry shell
poetry run python main.py
```
## GUI
It is mainly a terminal based application but a gui is in development

## Caution
This is a work in progress so use at your own risk

## License
Since it is completely open-source, use it as you please.
