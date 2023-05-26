# Import packages
import json
import os


# Execute commands given in JSON file
def executeJSON(jsonstr):
    responses = []

    # JSON commandos uitlezen
    dict_commands = readJSON(jsonstr)

    # Go trough each command
    for item in dict_commands["commands"]:
        result = os.popen(item["command"]).read()
        responses.append(result)

    # Return array of responses
    return responses


# Reads json files and returns dictionary
def readJSON(jsonstr):
    return json.loads(jsonstr)
