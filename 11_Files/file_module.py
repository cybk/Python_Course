class fl:
    def __init__(self, fileName):
        self.fileName = fileName

    def saveFile(self, data):
        with open(self.fileName, "wt") as flProcess:
            flProcess.write(data)

    def appendFile(self, data):
        with open(self.fileName, "at") as flProcess:
            flProcess.write(data)

    def readFile(self):
        with open(self.fileName, "rt") as flProcess:
            return flProcess.read()