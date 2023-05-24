# Repository lezen uit github


# Commandos uit github repo halen
def main():
    # Packages importeren
    from github import Github
    import os
    from dotenv import load_dotenv

    # ENV variabelen opehalen
    load_dotenv()
    GITHUB_TOKEN = os.getenv("TOKEN_GITHUB")

    g = Github(GITHUB_TOKEN)
    repo = g.get_user().get_repo("pythonproject")
    a = repo.get_contents("../commands.json")
    print(a.content)


if __name__ == "__main__":
    main()
