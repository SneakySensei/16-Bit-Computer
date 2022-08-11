import sys

# Open file using sys argument
with open(sys.argv[1]) as f:
  content = f.readlines()
# Remove trailing whitespaces
content = [x.strip().replace(" ", "") for x in content]

instructions = []  # List to hold instructions
output = []  # List to hold assembled machine instructions
outputHex = []

symbols = {"R0": "0", "R1": "1", "R2": "2", "R3": "3", "R4": "4", "R5": "5", "R6": "6", "R7": "7", "R8": "8", "R9": "9", "R10": "10",
           "R11": "11", "R12": "12", "R13": "13", "R14": "14", "R15": "15", "SCREEN": "16384", "KBD": "24576", "SP": "0", "LCL": "1",
           "ARG": "2", "THIS": "3", "THAT": "4"}

comp = {"0": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100", "A": "0110000", "M": "1110000",
        "!D": "0001101", "!A": "0110001", "!M": "1110001", "-D": "0001111", "-A": "0110011", "-M": "1110011",
        "D+1": "0011111", "A+1": "0110111", "M+1": "1110111", "D-1": "0001110", "A-1": "0110010", "M-1": "1110010",
        "D+A": "0000010", "D+M": "1000010", "D-A": "0010011", "D-M": "1010011", "A-D": "0000111", "M-D": "1000111",
        "D&A": "0000000", "D&M": "1000000", "D|A": "0010101", "D|M": "1010101"}

dest = {"M": "001", "D": "010", "MD": "011", "A": "100", "AM": "101", "AD": "110", "AMD": "111"}

jump = {"": "000", "JGT": "001", "JEQ": "010", "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}

varBaseAddress = 16

lineNumber = 0
# Removing inline and full line comments and whitespaces
for line in content:
    if (line and line[0] != '/'):
      if (line[0] != '('):
        instructions.append([x for x in line.split('//')][0].strip())
        lineNumber += 1
      else:
        symbols[line[1:-1]] = str(lineNumber)

def getSymbolValue(symbol):
  global varBaseAddress

  if (not symbols.get(symbol)):
    symbols[symbol] = str(varBaseAddress)
    varBaseAddress += 1

  return symbols[symbol]

def handleAInstruction(instruction):
  if (instruction[1:].isnumeric()):
    address = int(instruction[1:])  
  else:
    address = int(getSymbolValue(instruction[1:]))
  address = bin(address)[2:]       # Extract the binary of address
  machineCode = address.zfill(16)  # Make the instruction 16bit
  return machineCode

def handleCInstruction(instruction):
  destinationBits = "000"
  jumpBits = "000"
  machineCode = "111"

  instruction = instruction.split("=")
  if (len(instruction) == 2):
    destinationBits = dest[instruction[0]]
  instruction = instruction[-1].split(";")
  if (len(instruction) == 2):
    jumpBits = jump[instruction[1]]
  machineCode += comp[instruction[0]] + destinationBits + jumpBits
  return machineCode

# Start assembling instructions
for instruction in instructions:
  if (instruction[0] == '@'):
    output.append(handleAInstruction(instruction))
  else:
    output.append(handleCInstruction(instruction))

for line in output:
  outputHex.append(hex(int(line, 2))[2:].zfill(4))

print(outputHex)

# Save to new file
outputFile = sys.argv[1].split('/')[-1][0:-3] + "hack"
f = open(outputFile, "w+")
f.write("v2.0 raw\n")
f.write('\n'.join(outputHex))
f.close()