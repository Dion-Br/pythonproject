# Import packages
from modules.localmanager import Screenshot
from modules.remotecontroler import listener


# Main code
def main():
    # Initial startup:
    Screenshot()
    # Initial startup done
    # ---------------------
    # Listening to remote commands
    listener()


if __name__ == "__main__":
    main()
