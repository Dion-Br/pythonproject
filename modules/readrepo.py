# Commandos uit github repo halen
def readRemoteCommands():
    # Packages importeren
    from github import Github
    import os
    from dotenv import load_dotenv

    # ENV variabelen opehalen
    load_dotenv()
    GITHUB_TOKEN = os.getenv("TOKEN_GITHUB")

    g = Github(GITHUB_TOKEN)
    repo = g.get_user().get_repo("pythonproject")
    a = repo.get_contents("commands.json")
    return a.decoded_content
