"""
Turing Complete Language (brain f*ck clone)
Requirments:
 - Can move pointer
 - Can add or substract value
 - can loop 
 - can do i/o

"""
import os  # for file parsing
import sys  # for command line arguments

memory = [0] * 60000
varname = [0] * 2400
varvalue = [0] * 2400
varpos = 0
pos = 0
filename = sys.argv[1]
try:
    with open(str(filename), 'r') as d:
        lines = d.readlines()
except FileNotFoundError:
    print("File " + str(filename) + "not found!")
    exit()
print("File found!")
for i in range(len(lines)):
    if ("inc" in lines[i]):
        memory[pos] += 1
    elif ("dec" in lines[i]):
        memory[pos] -= 1
    elif ("out" in lines[i]):
        print(str(memory[pos]))
    elif ("inp" in lines[i]):
        (memory[pos]) = int(input(""))
    elif ("right" in lines[i]):
        pos += 1
    elif ("left" in lines[i]):
        if (pos != 0):
            pos -= 1
        else:
            print("Out of range! Ignored.")
    elif ("define" in lines[i]):
        vars = lines[i].split(' ')
        name = vars[1]
        varname[varpos] = name.strip("\n")
        varpos += 1
    elif ("set" in lines[i]):
        data = lines[i].split(' ')
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
                    if (value in varname):
                        memory[pos] = int(varvalue[varname.index(value)])
                    else:
                        memory[pos] = int(value)
                else:
                    print(name + " not found")
        else:
            varvalue[varname.index(name)] = memory[pos]
    elif ("push" in lines[i]):
        var = lines[i].split(' ')
        if (var[1].strip("\n") in varname):

            print(varvalue[varname.index(name)])
    elif ("goto" in lines):
        loc = lines[i].split(' ')[1]
        if (loc != "currentpoint"):
            if (loc in varname):
                pos = varvalue[varname.index(loc)]
            else:
                pos = int(loc)
        else:
            pos = memory[pos]
        memory[pos]
        print("Went to: " + loc)

    elif ("loop" in lines[i] and not "endloop" in lines[i]):
        i = i + 1
        times = lines[i]
        commandstorun = []
        while "endloop" not in lines[i]:
            commandstorun.append(lines[i])
            i += 1
        e = 0
        while e < int(times) - 1:
            e += 1
            for d in range(len(commandstorun)):
                if ("inc" in commandstorun[d]):
                    memory[pos] += 1
                elif ("dec" in commandstorun[d]):
                    memory[pos] -= 1
                elif ("out" in commandstorun[d]):
                    print(str(memory[pos]))
                elif ("inp" in commandstorun[d]):
                    (memory[pos]) = int(input(""))
                elif ("right" in commandstorun[d]):
                    pos += 1
                elif ("left" in commandstorun[d]):
                    if (pos != 0):
                        pos -= 1
                    else:
                        print("Out of range! Ignored.")
                elif ("define" in commandstorun[d]):
                    vars = commandstorun[d].split(' ')
                    name = vars[1]
                    varname[varpos] = name.strip("\n")
                    varpos += 1
                elif ("set" in commandstorun[d]):
                    data = commandstorun[d].split(' ')
                    name = data[1]
                    value = data[2].strip("\n")
                    if (value != "currentpoint"):
                        if name in varname:
                            if (value in varname):
                                varvalue[varname.index(name)] = varvalue[
                                    varname.index(value)]
                            else:
                                varvalue[varname.index(name)] = value

                        else:
                            if (name == "currentpoint"):
                                if (value in varname):
                                    memory[pos] = int(
                                        varvalue[varname.index(value)])
                                else:
                                    memory[pos] = int(value)
                            else:
                                print(name + " not found")
                    else:
                        varvalue[varname.index(name)] = memory[pos]

                elif ("push" in commandstorun[d]):
                    var = commandstorun[d].split(' ')
                    if (var[1].strip("\n") in varname):

                        print(varvalue[varname.index(name)])
                elif ("goto" in commandstorun[d]):
                    loc = commandstorun[d].split(' ')[1].strip("\n")
                    if (loc != "currentpoint"):
                        if (loc in varname):
                            pos = varvalue[varname.index(loc)]
                        else:
                            pos = int(loc)
                    else:
                        pos = int(memory[pos])
                    print("Went to: " + loc)

        i += len(commandstorun)
