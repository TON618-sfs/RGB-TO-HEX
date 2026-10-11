**English** | [Русский](README.ru.md)

# RGB TO HEX

A small desktop app that converts colors between **RGB(A)** and **HEX** in both directions. Built with Python and [Flet](https://flet.dev).

## Features

- RGB → HEX and HEX → RGB in two separate panels
- Optional alpha (transparency) channel in both directions
- Live color preview of the result
- Click the result to copy it to the clipboard
- Dark and light themes
- Buttons to clear a single result or all results at once

## Download (Windows)

Grab the installer or the standalone `.exe` from the [Releases](https://github.com/TON618-sfs/RGB-TO-HEX/releases/) page, or from the [`dist`](dist) folder of this repository. No Python needed.

> Windows may show a SmartScreen warning because the executable is not code-signed. Click **More info → Run anyway**.

## Run from source

You need Python 3 (the project was developed with Python 3.13).

**Install Python**

- Windows / macOS: download it from [python.org](https://www.python.org/downloads/)
- Arch Linux: `sudo pacman -S python python-pip`
- Debian / Ubuntu: `sudo apt install python3 python3-pip python3-venv`

**Get the code and start the app**

```bash
git clone https://github.com/TON618-sfs/RGB-TO-HEX.git
cd RGB-TO-HEX

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install flet==0.28.3
python "RGB TO HEX GUI/main.py"
```

On Linux use `python3` instead of `python` for the first `venv` command if `python` is not available. A virtual environment is recommended because some distributions (Arch, Debian 12+) refuse to install pip packages system-wide.

## How to use

**RGB to HEX.** Type three numbers (R, G, B) from 0 to 255, optionally followed by alpha from 0 to 1. Separate them with commas or spaces, then press **Enter** or click **Convert RGB to HEX**.

**HEX to RGB.** Type 6 digits (`RRGGBB`) or 8 digits (`RRGGBBAA`), with or without the leading `#`, then press **Enter** or click **Convert HEX to RGB**.

Alpha is always the last channel, as in CSS `#RRGGBBAA`.

| Input | Result |
|---|---|
| `128, 128, 128` | `#808080` |
| `106 13 173` | `#6a0dad` |
| `255, 0, 0, 0.5` | `#ff000080` |
| `808080` | `128, 128, 128` |
| `#6a0dad` | `106, 13, 173` |
| `80808080` | `128, 128, 128, 0.5` |

Click the result box to copy the value (without the `HEX code:` / `RGB code:` label).

## Project structure

```
RGB-to-HEX/
├── RGB TO HEX GUI/
│   ├── main.py                       # Flet interface
│   ├── rgb_to_hex.py                 # conversion functions
│   ├── icone.ico                     # app icon
│   ├── config for auto-py-to-exe/    # alternative build configs
│   └── config create installer/      # Inno Setup script for the installer
├── dist/                             # built .exe and installer
├── RGB TO HEX.spec                   # PyInstaller spec
├── LICENSE
├── README.md                         # description in English
└── README.ru.md                      # description in Russian
```

## Build the `.exe` and the installer

The executable is built with `flet pack` (it uses PyInstaller, so install it first if needed: `pip install pyinstaller`):

```bash
flet pack "RGB TO HEX GUI/main.py" -n "RGB TO HEX" -i "RGB TO HEX GUI/icone.ico"
```

The full command with version info and metadata is in `RGB TO HEX GUI/config for auto-py-to-exe/flet pack command.txt`.

The Windows installer is made with [Inno Setup](https://jrsoftware.org/isinfo.php) from `RGB TO HEX GUI/config create installer/RGB TO HEX.iss`. The paths inside the script point to the author's machine, so change them to your own before compiling.

## License

Released under the [MIT License](LICENSE). Copyright (c) 2026 TON618-sfs.
