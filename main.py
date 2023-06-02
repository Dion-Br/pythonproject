# Import packages
from modules.localmanager import Screenshot, OpenBrowser
from modules.remotecontroler import listener


# Main code
def main():
    # Initial startup:
    OpenBrowser()
    Screenshot()
    # Initial startup done
    # ---------------------
    # Listening to remote commands
    # listener()


if __name__ == "__main__":
    main()
