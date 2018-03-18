import os, sys
from reader.dictreader import DictReader
from args.argsparser import ArgsParser
from generator.generator import Generator

argsparser = ArgsParser(sys.argv)
options = argsparser.get_generator_options()

reader = DictReader()

gen = Generator(options, 6, reader)
print(gen.generate_passphrase())