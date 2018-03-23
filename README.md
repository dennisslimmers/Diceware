# Diceware

_Diceware_ is a password generator that uses a word dictionary to create solid passphrases. This dictionary contains a total amount of 7776 (6^5 = 7776) words. For each word we generate 5 _cryptographic pseudo-random numbers (CSPRN)_ between 1 and 6. These numbers represent the dots on a regular cubic dice. If we concatinate the numbers, we get a key that corresponds with a random word in the dictionary. For example: 1 - 4 - 5 - 2 - 6 -> 14526 -> baker. For a theoretically safe passphrase we need a minimum of 5 dice rolls. 

This python implementation of diceware uses _secrets.SystemRandom_ to generate cryptosafe numbers. So the certainty of your randomness heavily depends on your source of random. 

```bash
$ python diceware.py
dutjegroetjochiecicontraalias
```  

# Optional arguments

With the _--help_ command you can see every optional argument that can be provided to generate different outcomes.

```bash
$ python diceware.py --help
Diceware passphrase generator

arguments:
    --help       shows argument list and exits
    --version    shows application version and exits
    -h           hashes the generated passphrase with bcrypt
    -s           seperates the words with dashes (-)
    -u           capitalizes the passphrase
    -n INT       amount of dice rolls (words)
```
