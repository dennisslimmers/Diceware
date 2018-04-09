import os, sys

class DictReader: 
    def __init__(self, options):
        self.words = {}
        self.supported_languages = ["EN", "NL"] # TODO: add more dictionaries, currently only supporting dutch and english

        lang = str(options.get("-l")).upper()
        if (lang not in self.supported_languages):
            # Exit the application if a non valid language is provided
            print(lang + " is not a supported language!")
            exit(0)

        dict_name = "../dictionary/diceware_dict_" + lang + ".txt"
        file = open(dict_name, "r")
        lines = file.readlines()

        for line in lines:
            # Create a DictWord from the current line in the loop and add it to the words dictionary
            text = line.split("\t")
            
            if text[1].endswith('\n'):
                text[1] = text[1][:-1] # strip \n from the words

            self.words.update({ text[0]: text[1] })

    def preview(self, max):
        if len(self.words) > 0:
            counter = 0
            for key, value in self.words.items():
                if (counter != max):
                    print(key + ": " + value)
                else:
                    break

                counter = counter + 1

    def look_up(self, key):
        return self.words.get(key)


