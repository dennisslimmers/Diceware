import os, sys
from reader.dict_reader import DictReader
from args.argsparser import ArgsParser

argsparser = ArgsParser(sys.argv)
options = argsparser.get_generator_options()

reader = DictReader()
reader.preview()