def makeFile(results):
    with open("results.txt", "w") as file:
        for r in results:
            file.write(r)


def readFile(path):
    with open(path, "r") as file:
        return file.read()
