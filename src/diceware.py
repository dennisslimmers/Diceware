import os, sys

file_name = "../dictionary/diceware_dict_NL.txt"
file = open(file_name, "r")
lines = file.readlines()

def print_lines(lines):
    max = 5
    for i in range(0, 5):
        print(lines[i])

        if i == max:
            break

    end_script(lines)

def end_script(lines):
    end_script = input("Do you want to end the script? y/n: ")

    if end_script == "y":
        exit()
    else:
        print_lines(lines)

print_lines(lines)
