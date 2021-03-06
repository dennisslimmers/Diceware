import os, sys

class ArgsParser:
    def __init__(self, args):
        self.generator_options = {
            "-h": False,
            "-s": False,
            "-u": False,
            "-log": False,
            "-n": 6,
            "-l": "EN",
            "--version": "Diceware v0.1"
        }

        self.valid_commands = ["-h", "-s", "-u", "-n", "-l", "-log", "--help"]
        self.__args = args
        self.parse_args()

    def parse_args(self):
        for i in range(0, len(self.__args)):
            if i == 0:
                continue # The first arg is always the execution file, so skip it 
            else:
                if (self.__args[i] == "--help"):
                    self.show_help()
                    exit(0)
                elif (self.__args[i] == "--version"): # print the application version
                    print(self.generator_options.get("--version"))
                    exit(0)
                    
                if (self.__args[i].startswith("-")):
                    self.map_generator_option(self.__args[i], i)
            
    def map_generator_option(self, arg, i):
        if self.is_valid_argument(arg):
            if (arg == "-h"): # -h will hash the generated passphrase for more security (but less user friendly!)
                self.generator_options.update({ "-h": True })
            elif (arg == "-s"): # -s seperates the words with dashes (-)
                self.generator_options.update({ "-s": True })
            elif (arg == "-u"): # -u capitalizes the words
                self.generator_options.update({ "-u": True })
            elif (arg == "-log"): # -log logs the generated passphrase to a log file located in the logs folder
                self.generator_options.update({ "-log": True })
            elif (arg == "-n"): # number of words (dice rolls)
                try:
                    num = int(self.__args[(i + 1)])
                except:
                    e = sys.exc_info()[0]
                    print(e)
                    exit(0)
                
                self.generator_options.update({ "-n": num })
            elif (arg == "-l"): # dictionary language
                try:
                    lang = self.__args[(i + 1)]
                except:
                    e = sys.exc_info()[0]
                    print(e)
                    exit(0)
                
                self.generator_options.update({ "-l": lang })
        else:
            print(arg + " is not a valid argument, type --help for more information")
            exit(0)

    def is_valid_argument(self, arg):
        if arg not in self.valid_commands:
            return False
        else:
            return True

    def get_generator_options(self):
        return self.generator_options

    def show_help(self):
        help_msg = open("./../help.txt", "r").read() # Read the help message from the help.txt file
        print(help_msg)
                
