"""
Turing Complete Language (brain f*ck clone)
Requirments:
 - Can move pointer
 - Can add or substract value
 - can loop 
 - can do i/o
"""
import sys  # for command line arguments
import random

filename = sys.argv[1]
memory = [0] * 60000
varname = [0] * 2400
varvalue = [0] * 2400
varpos = 0
pos = 0
# Function 1
function1commands = [0] * 300
function1name = ""
functionargs = [0] * 5
ifstatments = []
DEBUG = True
DEBUGIF = True
DEBUG_LIST_ERROR = True
def dumpmemory():
    with open("dump.log", "w") as w:
        w.write("[VARNAME]\n")
        w.writelines(str(varname))
        w.write("\n[VARVALUE]\n")
        w.writelines(str(varvalue))
        w.write("\n[VARPOS]\n")
        w.write(str(varpos))
        w.write("\n[COMMANDS]\n")
        w.write(str(lines))
        w.write("\n[COMMANDS LENGTH]\n")
        w.write(str(len(lines)))
        w.write("\n[MEMORY]\n")
        w.write(str(memory))
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\u001b[37m'
    ERROR = '\u001b[31m'
bcolors = bcolors()

# if commands
def parsecommands(commands):
    
    global memory
    global varname
    global varvalue
    global varpos
    global pos
    global function1name
    global functionargs
    global function1commands
    #global ifstatments
    if(DEBUG):
        print(f'\n{bcolors.OKBLUE}{bcolors.BOLD}{bcolors.UNDERLINE}PARSING COMMANDS')
        print(f'\n{bcolors.OKBLUE}{bcolors.BOLD}{bcolors.UNDERLINE}LENGTH OF FILE IS {str(len(commands))}')
        print(bcolors.ENDC)
        print()
        print()
    for i in range(len(commands)):

        if (DEBUG):
            print(f'{bcolors.WHITE}')
            print(f'{bcolors.WHITE} I is: ', end='')
            print(f'{bcolors.WARNING}{i}', end=f'{bcolors.WHITE} command is: ')
            print(f'{bcolors.OKGREEN} {commands[i]}', end=f'{bcolors.WHITE} command outputed: {bcolors.OKBLUE}')
        if (commands[i] == 0):
            print("Weird error occuring..")
        if ("inc" in commands[i]):
            memory[pos] += 1
        elif ("dec" in commands[i]):
            memory[pos] -= 1
        elif ("out" in commands[i]):
            print(str(memory[pos]))
        elif ("inp" in commands[i]):
            (memory[pos]) = int(input(""))
        elif ("right" in commands[i]):
            pos += 1
        elif ("left" in commands[i]):
            if (pos != 0):
                pos -= 1
            else:
                print("Out of range! Ignored.")
        elif ("define" in commands[i]):
            vars = commands[i].split(' ')
            name = vars[1]
            if(DEBUG_LIST_ERROR):
                print(f'{bcolors.OKBLUE} varpos = {varpos}')
                print(f'Length = {len(varname)}')
            varname[varpos] = name.strip("\n")
         
            varpos += 1
        elif ("set" in commands[i]):
            data = commands[i].split(' ')
            name = data[1]
            value = data[2].strip("\n")
            if (value != "currentpoint"):
                if name in varname:
                    if (value == "random"):
                        varvalue[varname.index(name)] = random.randint(0, 100)
                    elif (value in varname):
                        varvalue[varname.index(name)] = varvalue[varname.index(
                            value)]
                    else:
                        varvalue[varname.index(name)] = value
                else:
                    if (name == "currentpoint"):
                        print(name + "Name")
                        print(value + " Value")
                        if (value in varname):
                            memory[pos] = int(varvalue[varname.index(value)])
                        else:
                            memory[pos] = int(value)
                    else:
                        print(name + " not found")
            else:
                varvalue[varname.index(name)] = memory[pos]
        elif ("push" in commands[i]):
            var = commands[i].split(' ')
            if (var[1].strip("\n") in varname):
                print(varvalue[varname.index(name)])
        elif ("goto" in commands[i]):
            loc = commands[i].split(' ')[1]
            if (loc != "currentpoint"):
                if (loc in varname):
                    pos = varvalue[varname.index(loc)]
                else:
                    pos = int(loc)
            else:
                pos = memory[pos]
            memory[pos]
            print("Went to: " + loc)
        elif ("function" in commands[i]):
            types = commands[i].split(' ')
            funcname = types[1]
            funcarg = types[2].strip(")")
            funcarg = funcarg.strip("(")
            function1name = funcname
            while ("endfunc" not in commands[i]):
                function1commands.append(commands[i])
                i += 1
        elif ("print" in commands[i]):
            out = commands[i].split(' ', 1)
            if (out[1].strip("\n") in varname):
                print(varvalue[varname.index(name)])
            else:
                print(out[1])
        elif ("if" in commands[i] and "endif" not in commands[i]):
            if(DEBUGIF):
                print(f'{bcolors.WARNING} \nif start', end=f'{bcolors.WHITE}\n')
            ifcommands = []
            istrue = False
            loc = commands[i].split(' ')
            loc3 = "".join(loc[3].split())
            loc1 = "".join(loc[1].split())  
            if(DEBUGIF):
                print('\ni should = ', end='')
                print(i, end=' ')
                print('right now.')
            if (loc1 in varname):
                if (loc[2] == "=="):
                    if (loc3 in varname):
                        if varvalue[varname.index(loc1)] == varvalue[
                                varname.index(loc3)]:
                            istrue = True
                elif (loc[2] == "!="):
                    if (loc3 in varname):
                        if varvalue[varname.index(
                                loc[1])] != varvalue[varname.index(loc3)]:
                            istrue = True
                elif (loc[2] == ">="):
                    if (loc[3] in varname):
                        if varvalue[varname.index(
                                loc[1])] >= varvalue[varname.index(loc[3])]:
                            istrue = True

                elif (loc[2] == "<="):
                    if (loc3 in varname):
                        if varvalue[varname.index(
                                loc[1])] <= varvalue[varname.index(loc3)]:
                            istrue = True

                elif (loc[2] == ">"):
                    if (loc3 in varname):
                        if varvalue[varname.index(
                                loc[1])] > varvalue[varname.index(loc3)]:
                            istrue = True
                elif (loc[2] == "<"):
                    if (loc3 in varname):
                        if varvalue[varname.index(
                                loc[1])] < varvalue[varname.index(loc3)]:
                            istrue = True
                else:
                    print("Incorrect Syntax")
               
                while ("endif" not in commands[i]):
                    i += 1
                    ifcommands.append(commands[i])
                    ifstatments.append(i)
                    if(DEBUGIF):             
                        print("           Incremented i: ", end='')
                        print(i, end=', command was: ')
                        print(commands[i])
                if (istrue):
                    if(DEBUGIF):
                        print("Is True")
                    parsecommands(ifcommands)
                if(DEBUGIF):
                    print(f'{bcolors.WARNING} \nif end', end=f'{bcolors.WHITE}\n')

        elif ("loop" in commands[i] and not "endloop" in commands[i]):
            bruh = commands[i].split(' ')
            try:
                times = bruh[1].strip("\n")
            except Exception as excep:
                print(f"Incorrect syntax on line {i+2}")
            commandstorun = []
            i += 1
            while "endloop" not in commands[i]:
                commandstorun.append(commands[i])
                i += 1
            e = 0
            while e < int(times) - 1:
                parsecommands(commandstorun)
                e += 1
        else:
            if (commands[i].strip("\n") == function1name):
                parsecommands(function1commands)

try:
    with open(str(filename), 'r') as d:
        lines = d.readlines()
except FileNotFoundError:
    print("File " + str(filename) + "not found!")
    exit()
print("File found! Running..")
for e in range(len(lines)):
    lines[e] = lines[e].strip("\n")
try:
    parsecommands(lines)
except Exception as exc:
   print(f'Error: {bcolors.ERROR}{exc}', end = f'{bcolors.WHITE}\n')
   dumpmemory()
   print(bcolors.ENDC)


print(bcolors.ENDC)