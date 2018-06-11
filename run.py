import os, sys, datetime, pyperclip
from diceware.dictreader import DictReader
from diceware.argsparser import ArgsParser
from diceware.generator import Generator
from diceware.timer import Timer
from diceware.logger import Logger

from diceware.argsparser import ArgsParser

def log(logger, datetime, passphrase):
    logger.write(datetime, passphrase)


def init():
    argsparser = ArgsParser(sys.argv)
    options = argsparser.get_generator_options()
    reader = DictReader(options)

    timer = Timer()
    timer.start()

    gen = Generator(options, reader)
    passphrase = gen.generate_passphrase()
    
    pyperclip.copy(passphrase) # Copy the passphrase to the users clipboard

    print('''
     ____  _                                 
    / __ \(_)_______ _      ______ _________ 
   / / / / / ___/ _ \ | /| / / __ `/ ___/ _ \\
  / /_/ / / /__/  __/ |/ |/ / /_/ / /  /  __/
 /_____/_/\___/\___/|__/|__/\__,_/_/   \___/
    ''')

    print("Started generating at: " + str(timer.start))
    print(timer.stop())
    print(timer.elapsed())
    print("\nPassphrase: " + str(passphrase))
    print("The passphrase is copied to your clipboard, press CTRL + V to paste")
    
    if (options.get("-log")):
        logger = Logger()
        log(logger, datetime.datetime.now(), passphrase)


if (__name__ == "__main__"):
    init() # Initialise 