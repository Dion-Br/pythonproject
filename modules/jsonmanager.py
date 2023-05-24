import json


def executeJSON(jsonstr):
    # JSON commandos uitlezen
    dict_commands = readJSON(jsonstr)
    print(dict_commands["commandos"])


def readJSON(jsonstr):
    return json.loads(jsonstr)
