import os, sys

class DictReader: 
    def __init__(self):
        self.words = {}
        dict_name = "../dictionary/diceware_dict_NL.txt"
        file = open(dict_name, "r")
        lines = file.readlines()

        for line in lines:
            # Create a DictWord from the current line in the loop and add it to the words dictionary
            text = line.split("\t")
            
            if text[1].endswith('\n'):
                text[1] = text[1][:-1] # strip \n from the words

            self.words.update({text[0]: text[1]})

    def preview(self, max):
        if len(self.words) > 0:
            counter = 0
            for key, value in self.words.items():
                if (counter != max):
                    print(key + ": " + value)
                else:
                    break

                counter = counter + 1


