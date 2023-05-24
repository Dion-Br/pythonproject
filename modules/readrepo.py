# Repository lezen uit github
from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("TOKEN_GITHUB")


def main():
    g = Github(GITHUB_TOKEN)
    repo = g.get_user().get_repo("pythonproject")
    a = repo.get_contents("README.md")
    print(a.content)


if __name__ == "__main__":
    main()
