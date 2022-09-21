import sys  # for command line arguments
import random

filename = sys.argv[1]

# if commands
def parsecommands(commands):
    pass
try:
    with open(str(filename), 'r') as d:
        lines = d.readlines()
except FileNotFoundError:
    print("File " + str(filename) + " not found!")
    exit()
print("File found! Running..")
for e in range(len(lines)):
    lines[e] = lines[e].strip("\n")
try:
    parsecommands(lines)
except Exception as exc:
   print("error lol")
