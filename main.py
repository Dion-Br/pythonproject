from modules.readrepo import readRemoteCommands
from modules.jsonmanager import executeJSON


# Main code
def main():
    executeJSON(readRemoteCommands())


if __name__ == "__main__":
    main()
