import sys, os

class Logger:
    def __init__(self):
        try:
            self.file = open("../logs/genlog.txt", 'a')
        except IOError as E:
            print(E) # No such file or directory: '../logs/genlog.txt'
            exit(0)
    
    def write(self, dateTime, passphrase):
        self.file.write("generated " + str(passphrase) + " on " + str(dateTime) + "\n")