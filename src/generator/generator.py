import os, sys, bcrypt
from random import SystemRandom
from reader.dictreader import DictReader

class Generator:
    def __init__(self, options, dice_rolls, dictreader):
        self.options = options
        self.dice_rolls = dice_rolls
        self.dictreader = dictreader
    
    def generate_passphrase(self):
        '''
        So for each word we need to generate 5 cryptosafe random numbers between 1 and 6. These numbers 
        concatinated create the key that corresponds with the word in the dictionary, 
        for example: 4 - 5 - 1 - 2 - 6 = 45126 = hemels. These words essentially form the passphrase
        '''

        passphrase = ""
        for i in range(0, self.dice_rolls):
            key = ""  # dictionary key
            for n in range(0, 5):
                key += str(self.random())

            word = self.dictreader.look_up(key)

            # If the -s argument is provided, add dashes between every generated word
            if self.options.get("-s"):
                passphrase += ("-" if i != 0 else "") + word
            else:
                passphrase += word

        # If the -u argument is provided, capitalize the passphrase
        passphrase = passphrase.upper() if self.options.get("-u") else passphrase

        # If the -e argument is provided, hash the passphrase with Bcrypt
        passphrase = self.hash(passphrase) if self.options.get("-h") else passphrase 

        return passphrase        

    def random(self):
        cryptogen = SystemRandom()

        # Generate a cryptosafe number between 1 and 6
        return cryptogen.randrange(1, 6) 

    def hash(self, passphrase):
        # Hash the passphrase with bcrypt
        return bcrypt.hashpw(passphrase.encode("utf-8"), bcrypt.gensalt())



