"""
Turing Complete Language (brain f*ck clone)
Requirments:
 - Can move pointer
 - Can add or substract value
 - can loop 
 - can do i/o
"""
import sys  # for command line arguments

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
    for i in range(len(commands)):
        if (commands[i] == 0):
            exit()
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
            varname[varpos] = name.strip("\n")
            varpos += 1
        elif ("set" in commands[i]):
            data = commands[i].split(' ')
            name = data[1]
            value = data[2].strip("\n")
            if (value != "currentpoint"):
                if name in varname:
                    if (value in varname):
                        varvalue[varname.index(name)] = varvalue[varname.index(
                            value)]
                    else:
                        varvalue[varname.index(name)] = value

                else:
                    if (name == "currentpoint"):
                        print(name + "Name") # var.tc returns currentpoint
                        print(value + " Value") # var.tc returns based
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
                print(varvalue[varname.index(name)]) # var.tc: error currentpoint is not in list
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
        elif ("if" in commands[i] and "endif" not in commands[i]):
            print(f"Ran if statement")
            ifcommands = []
            istrue = False
            loc = commands[i].split(' ')
            loc3 = "".join(loc[3].split()) #index out of range error
            loc1 = "".join(loc[1].split()) #probably will happen here to
            if (loc1 in varname):
                if (loc[2] == "=="):
                    if (loc3 in varname):
                        if varvalue[varname.index(loc1)] == varvalue[varname.index(loc3)]:
                            istrue = True
                        else:
                            print("False")
                elif (loc[2] == "!="):
                    if (loc3 in varname):
                        if varvalue[varname.index(loc[1])] != varvalue[varname.index(loc3)]:
                            istrue = True
                        else:
                            print("False")
                elif (loc[2] == ">="):
                    if (loc[3] in varname):
                        if varvalue[varname.index(loc[1])] >= varvalue[varname.index(loc[3])]:
                            istrue = True
                        else:
                            print("False")
                elif (loc[2] == "<="):
                    if (loc3 in varname):
                        if varvalue[varname.index(loc[1])] <= varvalue[varname.index(loc3)]:
                            istrue = True
                        else:
                            print("False")
                elif (loc[2] == ">"):
                    if (loc3 in varname):
                        if varvalue[varname.index(loc[1])] > varvalue[varname.index(loc3)]:
                            istrue = True
                        else:
                            print("False")
                elif (loc[2] == "<"):
                    if (loc3 in varname):
                        if varvalue[varname.index(loc[1])] < varvalue[varname.index(loc3)]:
                            istrue = True
                        else:
                            print("False")
                else:
                    print("Incorrect Syntax")
                i += 1
                while ("endif" not in commands[i]):
                    ifcommands.append(commands[i])
                    i += 1
                if(istrue):
                    print("END IF WORKING")
                    parsecommands(ifcommands)
                print(f"Ran if statement with and output of {istrue}")
        elif ("loop" in commands[i] and not "endloop" in commands[i]):
            bruh = commands[i].split(' ')
            times = bruh[1].strip("\n")
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
        print(f"Command: {commands[i]}")

try:
    with open(str(filename), 'r') as d:
        lines = d.readlines()
except FileNotFoundError:
    print("File " + str(filename) + "not found!")
    exit()
print("File found!")
for e in range(len(lines)):
    lines[e] = lines[e].strip("\n")
parsecommands(lines)
