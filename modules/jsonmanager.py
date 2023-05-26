import json
import os


def executeJSON(jsonstr):
    responses = []

    # JSON commandos uitlezen
    dict_commands = readJSON(jsonstr)

    for item in dict_commands["commands"]:
        result = os.popen(item["command"]).read()
        responses.append(result)

    return responses


def readJSON(jsonstr):
    return json.loads(jsonstr)
