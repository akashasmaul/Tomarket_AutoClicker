# Tomarket_AutoClicker

## Tomarket Clicker Bot

A Python-based auto-clicker bot that hovers over reddish (tomato) elements in the Telegram Desktop app. This bot uses `pynput` to simulate mouse movements and detects specific colors on the screen to interact with the application.

### Features:
- **Window Activation**: Automatically finds and activates the Telegram Desktop window.
- **Color Detection**: Hovers over regions that match a specified reddish color range.
- **Keyboard Controls**: Pause or resume the bot by pressing the `Space` key.
- **Customizable Logic**: Define color ranges to exclude specific elements (e.g., bomb fire portion).

### Requirements:
- Python 3.10
- `pynput`
- `pygetwindow`
- `pyautogui`
- `keyboard`
  
Windows:
```shell
run.bat
```

Windows:
```shell
Tomatar.exe
```

### Usage:
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Press `Space` to start or pause the bot.

---
