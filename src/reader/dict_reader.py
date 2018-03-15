import os, sys

class DictReader: 
    def __init__(self):
        self.words = []
        dict_name = "../dictionary/diceware_dict_NL.txt"
        file = open(dict_name, "r")
        lines = file.readlines()

        for line in lines:
            # Create a DictWord from the current line in the loop and add it to the words list
            text = line.split("\t")
            self.words.append(text)

    def preview(self):
        if len(self.words) > 0:
            max = 5

            for i in range(0, max):
                print(self.words[i][1])


