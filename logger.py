import datetime

class Logger:
    def __init__(self, filename):
        self.logfile = open(filename, "w")
        self.meme = "Hi"
    
    def log(self, content):
        self.logfile.write(content)

    def __del__(self):
        self.logfile.close()