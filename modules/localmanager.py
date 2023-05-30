# Local Manager: Executing initial tasks on local machine
import pyautogui
import os


def Screenshot():
    ss = pyautogui.screenshot()
    cd = os.getcwd()
    print(cd)  # Check if the path it
    # specifying is correct
    ss.save(cd + "../Screenshot.png")
