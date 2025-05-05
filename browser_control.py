import pyautogui
import time

def click_at(x, y):
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.click()

def type_text(text):
    pyautogui.write(text, interval=0.05)

def take_screenshot(path="screenshot.png"):
    img = pyautogui.screenshot()
    img.save(path)
    return path
