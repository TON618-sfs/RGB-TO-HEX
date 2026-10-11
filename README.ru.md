[English](README.md) | **Русский**

# RGB TO HEX

Небольшая десктопная программа, которая переводит цвета между **RGB(A)** и **HEX** в обе стороны. Написана на Python с помощью [Flet](https://flet.dev).

## Возможности

- RGB → HEX и HEX → RGB в двух отдельных блоках
- Необязательный альфа-канал (прозрачность) в обе стороны
- Превью цвета результата
- Клик по результату копирует его в буфер обмена
- Тёмная и светлая темы
- Кнопки для очистки одного результата или сразу всех

Интерфейс программы на английском языке.

## Скачать (Windows)

Установщик или отдельный `.exe` можно скачать на странице [Releases](https://github.com/TON618-sfs/RGB-TO-HEX/releases/) или из папки [`dist`](dist) в этом репозитории. Python для этого не нужен.

> Windows может показать предупреждение SmartScreen, потому что `.exe` не подписан сертификатом. Нажми **Подробнее → Выполнить в любом случае**.

## Запуск из исходников

Нужен Python 3 (проект разрабатывался на Python 3.13).

**Установка Python**

- Windows / macOS: скачай с [python.org](https://www.python.org/downloads/)
- Arch Linux: `sudo pacman -S python python-pip`
- Debian / Ubuntu: `sudo apt install python3 python3-pip python3-venv`

**Скачать код и запустить**

```bash
git clone https://github.com/TON618-sfs/RGB-TO-HEX.git
cd RGB-TO-HEX

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install flet==0.28.3
python "RGB TO HEX GUI/main.py"
```

В Linux для первой команды с `venv` используй `python3` вместо `python`, если `python` не найден. Виртуальное окружение лучше не пропускать: некоторые дистрибутивы (Arch, Debian 12+) не дают ставить pip-пакеты в систему напрямую.

## Как пользоваться

**RGB → HEX.** Введи три числа (R, G, B) от 0 до 255, при желании добавь четвёртое: альфа-канал от 0 до 1. Разделяй их запятыми или пробелами, затем нажми **Enter** или кнопку **Convert RGB to HEX**.

**HEX → RGB.** Введи 6 цифр (`RRGGBB`) или 8 цифр (`RRGGBBAA`), с символом `#` или без него, затем нажми **Enter** или кнопку **Convert HEX to RGB**.

Альфа-канал всегда стоит последним, как в CSS-формате `#RRGGBBAA`.

| Ввод | Результат |
|---|---|
| `128, 128, 128` | `#808080` |
| `106 13 173` | `#6a0dad` |
| `255, 0, 0, 0.5` | `#ff000080` |
| `808080` | `128, 128, 128` |
| `#6a0dad` | `106, 13, 173` |
| `80808080` | `128, 128, 128, 0.5` |

Клик по полю с результатом копирует значение (без подписи `HEX code:` / `RGB code:`).

## Структура проекта

```
RGB-to-HEX/
├── RGB TO HEX GUI/
│   ├── main.py                       # интерфейс на Flet
│   ├── rgb_to_hex.py                 # функции конвертации
│   ├── icone.ico                     # иконка программы
│   ├── config for auto-py-to-exe/    # альтернативные конфиги сборки
│   └── config create installer/      # скрипт Inno Setup для установщика
├── dist/                             # собранные .exe и установщик
├── RGB TO HEX.spec                   # спецификация PyInstaller
├── LICENSE
├── README.md                         # описание на английском
└── README.ru.md                      # описание на русском
```

## Сборка `.exe` и установщика

`.exe` собирается командой `flet pack` (под капотом она использует PyInstaller, так что при необходимости сначала поставь его: `pip install pyinstaller`):

```bash
flet pack "RGB TO HEX GUI/main.py" -n "RGB TO HEX" -i "RGB TO HEX GUI/icone.ico"
```

Полная команда с версией и метаданными лежит в файле `RGB TO HEX GUI/config for auto-py-to-exe/flet pack command.txt`.

Установщик для Windows делается в [Inno Setup](https://jrsoftware.org/isinfo.php) из скрипта `RGB TO HEX GUI/config create installer/RGB TO HEX.iss`. Пути внутри скрипта ведут на компьютер автора, поэтому перед компиляцией замени их на свои.

## Лицензия

Проект распространяется по лицензии [MIT](LICENSE). Copyright (c) 2026 TON618-sfs.
