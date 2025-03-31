# Игра "Виселица" на Python

Две версии игры:
1. Консольная (`hangman_console.py`)
2. Графическая с tkinter (`hangman_gui.py`)

## Как запустить?
### Консольная версия
```bash
python hangman_console.py
```

### Графическая версия (требуется tkinter)
```bash
python hangman_gui.py
```

## Особенности
- Угадывание животных
- 6 попыток
- Поддержка русского языка

![Скриншот игры](screenshot.png)  # Добавьте позже скриншот

## 📥 Скачать игру
Готовую версию для Windows можно скачать [здесь](dist/Viselica.exe).

## 🔨 Сборка из исходников
```bash
pip install pyinstaller
pyinstaller --onefile --windowed src/hangman_gui.py
```
