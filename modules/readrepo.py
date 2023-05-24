# Repository lezen uit github
from github import Github


def main():
    g = Github("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")
    repo = g.get_user().get_repo("pythonproject")
    a = repo.get_contents("README.md")
    print(a.content)


if __name__ == "__main__":
    main()
