from cx_Freeze import setup, Executable

base = None    

executables = [Executable("src/diceware.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "diceware",
    options = options,
    version = "0.1",
    description = 'Diceware Passphrase Generator',
    executables = executables
)