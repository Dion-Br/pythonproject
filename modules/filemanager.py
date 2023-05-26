# File manager: Write and read files on local machine


# Make a file with the given results
def makeFile(results):
    with open("results.txt", "w") as file:
        for r in results:
            file.write(r)


# Read file
def readFile(path):
    with open(path, "r") as file:
        return file.read()
