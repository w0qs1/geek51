# CAUTION
# This project is under development and this file is not for use currently

dhexcode = []
dnobytes = []
dmnemonic = []
doperands = []

f = open("test.asm", "r") # example assembly file
asm = f.readlines()
f.close()

c = open("opcodehex.txt", "r") # op code definition file
for line in c.readlines():
    if "Hex" in line or "reserved" in line: # skip the first line and reserved opcode
        continue

    splitline = line.split(" ")

    dhexcode += splitline[0]
    dnobytes += splitline[1]
    dmnemonic += splitline[2]
    doperands += splitline[3]

c.close()

org = [] # to store the address parameters from ORG

for index, line in enumerate(asm):
    line = line.strip() # strip extra spaces at the beginning and at the end

    if ";" in line: # remove any comments
        line = line[:line.find(";")].rstrip()

    if ["ORG", "org"] in line: # get the address
        org += line[4:]

    if ["END", "end"] in line: # exit this loop
        break

    if ":" in line: # get the label if it exists
        label = line[:line.find(":") + 1]
        line = (line[line.find(":") + 1:]).lstrip() # removes the label and :

    q = 0
    for i, v in enumerate(line):
        if v == " " or v == ",": # skip the space and comma
            q = 1 # set q
            # this can be done once because the opcode has no spaces
            continue

        elif q == 0: # if q is clear, store it into opcode
            opcode += v
        
        elif q == 1: # if q is set, store it into operands
            operands += v