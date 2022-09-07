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
      i += len(commandstorun)
