import asyncio
import random
from itertools import product
from pynput.mouse import Button, Controller
import pygetwindow as gw
import pyautogui
import keyboard
import time


class Clicker:
    def __init__(self):
        self.mouse = Controller()
        self.window_name = 'TelegramDesktop'
        self.paused = True
        self.window = None
        self.window_found = False  # Flag to track if the window has been found and activated

    def activate_window(self):
        """
        Activate the Telegram window if it hasn't been activated yet.
        """
        if not self.window_found:  # Only activate if not already done
            check = gw.getWindowsWithTitle(self.window_name)
            if not check:
                print(f'[❌] | Window - {self.window_name} not found! Please open Telegram.')
                return None
            
            telegram_window = check[0]
            print(f'[✅] | Found Telegram window: {self.window_name}')
            try:
                telegram_window.activate()
                print(f'[🔄] | Activated Telegram window: {self.window_name}')
            except:
                telegram_window.minimize()
                telegram_window.restore()
                print(f'[⚠️] | Restored and activated minimized Telegram window: {self.window_name}')

            self.window_found = True  # Set the flag so it doesn't print repeatedly
            return telegram_window
        else:
            return gw.getWindowsWithTitle(self.window_name)[0]

    async def handle_input(self) -> bool:
        """
        Handles pausing and resuming the script using keyboard input.
        Press 'Space' to start/resume and again 'Space' to pause.
        """
        if keyboard.is_pressed("space") and self.paused:
            self.paused = False
            print("▶️ Thread Initiated! Press 'space' to pause.")
            await asyncio.sleep(0.2)

        elif keyboard.is_pressed("space"):
            self.paused = not self.paused
            print("⏸️ Paused! Press 'space' to resume." if self.paused else "▶️ Started! Press 'space' to pause.")
            await asyncio.sleep(0.2)

        return self.paused

    async def hover_on_color_match(self, screen, rect, color_range) -> bool:
        """
        Search for a color that matches the specified range and hover the mouse over it.
        """
        width, height = screen.size

        for x, y in product(range(0, width, 20), range(0, height, 20)):
            r, g, b = screen.getpixel((x, y))
            if color_range(r, g, b):
                screen_x = rect[0] + x
                screen_y = rect[1] + y
                
                # Move the mouse to the detected location
                self.mouse.position = (screen_x + 4, screen_y)
                return True
        return False

    def capture_screenshot(self, window):
        """
        Capture the screenshot of the active window's region.
        """
        rect = (window.left, window.top, window.width, window.height)
        return pyautogui.screenshot(region=rect), rect

    async def run(self) -> None:
        """
        Main function to run the script.
        """
        start_text = """   
                 
▄▄▄█████▓ ▒█████   ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓ ▒█████       ██████  ██▓    ▄▄▄        ██████  ██░ ██ 
▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒   ▒██    ▒ ▓██▒   ▒████▄    ▒██    ▒ ▓██░ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒   ░ ▓██▄   ▒██░   ▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░
░ ▓██▓ ░ ▒██   ██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░     ▒   ██▒▒██░   ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ 
  ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░   ▒██████▒▒░██████▒▓█   ▓██▒▒██████▒▒░▓█▒░██▓
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
    ░      ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░   ░      ░ ▒ ▒░    ░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░
  ░      ░ ░ ░ ▒  ░      ░     ░   ▒    ░      ░ ░ ░ ▒     ░  ░  ░    ░ ░    ░   ▒   ░  ░  ░   ░  ░░ ░
             ░ ░         ░         ░  ░            ░ ░           ░      ░  ░     ░  ░      ░   ░  ░  ░
                                                                                                      
                                                                                                                                   """
        print(start_text)
        print("")
        print("Requesting TON: UQDdaLRhnK9dKSgOSQ9IVXGGM_RVUu3mv_16-400XMiA6ZBz")
        print("GitHub: https://github.com/akashasmaul")
        print("\nHit the 'Space' to start smashing")

        while True:
            if await self.handle_input():
                continue

            window = self.activate_window()
            if not window:
                continue

            # Capture screenshot of the Telegram window
            screenshot, rect = self.capture_screenshot(window)

            def reddish_range(r, g, b):
                # Define a range that matches reddish colors, but exclude the bomb's fire
                is_reddish = (150 <= r <= 255) and (g < 150) and (b < 150)
    
                # Exclude fire-like colors (adjust RGB values if necessary for fire portion)
                is_bomb_fire = (200 <= r <= 255) and (100 <= g <= 200) and (0 <= b <= 100)

                return is_reddish and not is_bomb_fire


            # Create tasks for concurrent execution
            tasks = [self.hover_on_color_match(screenshot, rect, reddish_range) for _ in range(10)]

            # Execute tasks concurrently
            await asyncio.gather(*tasks)
            
            # Delay to avoid high CPU usage
            await asyncio.sleep(0.01)


# Main execution
if __name__ == "__main__":
    clicker = Clicker()
    asyncio.run(clicker.run())
