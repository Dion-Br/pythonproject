# Import packages
from modules.repomanager import readRemoteCommands, writeToRepo
from modules.jsonmanager import executeJSON
from modules.filemanager import makeFile


# Main code
def main():
    # Get commands from github repo
    result = executeJSON(readRemoteCommands("commands.json"))
    # Read the hostname from the local machine
    hostname = result[1].splitlines()[1].split()[2]
    # Make a file with the given results
    makeFile(result)
    # Write the file to github
    writeToRepo("results.txt", hostname)


if __name__ == "__main__":
    main()
