import os, sys

class ArgsParser:
    def __init__(self, args):
        self.generator_options = {
            "-e": False,
            "-s": False,
        }

        self.valid_commands = ["-e", "-s"]
        self.__args = args
        self.parse_args()

    def parse_args(self):
        for i in range(0, len(self.__args)):
            if i == 0:
                continue # The first arg is always the execution file, so skip it 
            else:
                self.map_generator_option(self.__args[i])
            
    def map_generator_option(self, arg):
        if self.is_valid_argument(arg):
            if (arg == "-e"): # -e will hash the generated passphrase for more security (but less user friendly!)
                self.generator_options.update({ "-e": True })
            elif (arg == "-s"): # -s seperates the words with dashes (-)
                self.generator_options.update({ "-s": True })
        else:
            print(arg + " is not a valid argument!")
            exit(0)

    def is_valid_argument(self, arg):
        if arg not in self.valid_commands:
            return False
        else:
            return True

    def get_generator_options(self):
        return self.generator_options
                
