import os, sys

class ArgsParser:
    def __init__(self, args):
        self.generator_options = []
        self.__args = args
        self.parse_args()

    def parse_args(self):
        for i in range(0, len(self.__args)):
            if i == 0:
                continue # The first arg is always the execution file, so skip it 
            else:
                self.map_generator_option(self.__args[i])
            
    def map_generator_option(self, arg):
        if (arg == "/e"): # /e will double encrypt the chosen word for more security (but less user friendly!)
            self.generator_options.append("encrypt")
        elif (arg == "/s"): # /s seperates the words with an underscore (_)
            self.generator_options.append("random_seperators")
        else:
            print(arg + " is not a valid argument!")
            exit(0)

    def get_generator_options(self):
        return self.generator_options
                
