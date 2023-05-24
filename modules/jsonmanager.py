import json
import os


def executeJSON(jsonstr):
    # JSON commandos uitlezen
    dict_commands = readJSON(jsonstr)

    for item in dict_commands["commands"]:
        print(f"Name: {item['name']} => Command: {item['command']} \nResult:")
        result = os.popen(item["command"]).read()
        print(result)


def readJSON(jsonstr):
    return json.loads(jsonstr)
