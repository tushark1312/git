file = open("INPUT CODE 6.txt")
lines= file.readlines()
tlines = []
for line in lines:
  tokens = line.split()
  tlines.append(tokens)
MNTP= 0
MDTP = 0
#Macro name, MDT pointer
MNT = []
#Definition
MDT = []
ALAA = []
#[[arg1, #1,]]
ALA = []

def formatString(word):
    return word.split(',')[0]

def prepALA(parameters):
  d = {}
  for i in range(len(parameters)):
    d[parameters[i]] = "#"+str(i+1)
  #print(d)
  return d

def formatLine(ALA, line):
  parameters = list(ALA.keys())
  for i in range(len(line)):
    if(line[i] in parameters):
      line[i] = ALA[line[i]]
  return (line)
i = 0
n = len(tlines)
for line in tlines:
    for i in range(len(line)):
        line[i] = formatString(line[i])
i=0
ALAPointer = 0
while(i < n):
  line = tlines[i]
  if(line[0] == 'MACRO'):
    MNT.append([line[1], MDTP])
    MDT.append(line)
    MDTP+=1
    ALA = prepALA(line[2:])
    ALAA.append(ALA)
    ALAPointer +=1
    j = i+1
    line = tlines[j]
    while(j < n and line[0] != 'MEND'):
      j+=1
      line = tlines[j]
      l = formatLine(ALA, line)
      MDT.append(l)
      MDTP+=1
    i = j
  elif(line[0] == 'MEND'):
    i+=1
    MDTP+=1
    MNTP+=1
  else:
    i+=1

print("MNT")
for i in MNT:
    print(i)
print("\nMDT")
for i in MDT:
    print(i)