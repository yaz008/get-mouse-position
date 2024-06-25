# Get Mouse Position

## Installation

First, clone the repository

```sh
git clone https://github.com/yaz008/EspScript
```

Then create Python 3.12 virtual environment, activate it and run

```sh
pip install -r requirements.txt
```

## Usage

Run `src/main.py` file using Python interpreter from the virtual environment

Hover the mouse cursor over an element you want to know position of and press `t`

Position of the mouse cursor will be printed to the console

## Customization

### Control Keys

Adjust the toggle and exit keys by passing different arguments to the `getter`

### Actions

Add your own actions in `src/actions.py` file, then adjust the imports in `src/main.py` and pass the action function as `action` parameter to the `getter`

## License

Get Mouse Position is an open-source software distributed under the [MIT License](LICENSE.txt)