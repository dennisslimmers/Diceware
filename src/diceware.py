import os, sys, datetime
from reader.dictreader import DictReader
from args.argsparser import ArgsParser
from generator.generator import Generator
from logging.timer import Timer
from logging.logger import Logger

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

    print("Started generating at: " + str(timer.start))
    print(timer.stop())
    print(timer.elapsed())
    print("\nPassphrase: " + str(passphrase))
    
    if (options.get("-log")):
        logger = Logger()
        log(logger, datetime.datetime.now(), passphrase)
        

if (__name__ == "__main__"):
    init() # Initialise 