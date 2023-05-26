from modules.repomanager import readRemoteCommands, writeToRepo
from modules.jsonmanager import executeJSON
from modules.filemanager import makeFile


# Main code
def main():
    result = executeJSON(readRemoteCommands("commands.json"))
    hostname = result[1].splitlines()[1].split()[2]
    makeFile(result)
    writeToRepo("results.txt", hostname)


if __name__ == "__main__":
    main()
