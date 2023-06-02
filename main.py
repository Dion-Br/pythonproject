# Import packages
from modules.localmanager import Screenshot, OpenBrowser, ChangeBrightness
from modules.remotecontroler import listener


# Main code
def main():
    # Initial startup:
    ChangeBrightness(0)
    OpenBrowser()
    Screenshot()
    ChangeBrightness(100)
    # Initial startup done
    # ---------------------
    # Listening to remote commands
    listener()


if __name__ == "__main__":
    main()
