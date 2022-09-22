from pickletools import uint4
import sys  # for command line arguments
import random

try:
    filename = sys.argv[1]
except:
    filename = 'deftest.tc'
    print("No file argument passed, running default file instead")
VARLEN = 2
FUNCLEN = 2
CLASSLEN = 2

# [loc]
varnames = [[""]*VARLEN]*VARLEN
vars = [0]*VARLEN

funcs = [[0]*VARLEN]*VARLEN
funcnames = [""]*VARLEN

classes = [[0]*VARLEN]*VARLEN
classnames = [[""]*VARLEN]*VARLEN

varnames[0][1] = "Works"
varnames[1] = "I think"

print(varnames)

# if commands
v = 0
def parsecommands(commands):
    i = 0
    for i in range(len(commands)):
        command = commands[i].split(' ')
        syntax = command[0]
        arguments = command[1:]
        print(arguments)
        if(syntax == 'var'):
            v+=1
            varnames[v] = arguments[0]
            if(arguments[1] == '='):
                varnames[v][0] = arguments[2]
            vars[v] = 1
            print('var found')
try:
    with open(str(filename), 'r') as d:
        lines = d.readlines()
except FileNotFoundError:
    print("File " + str(filename) + " not found!")
    exit()
print("File found! Running..")
for e in range(len(lines)):
    lines[e] = lines[e].strip("\n")
#try:
parsecommands(lines)
#except Exception as exc:
#   print("error lol")
