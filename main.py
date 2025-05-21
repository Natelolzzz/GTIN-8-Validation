import math, NateUtils

def makeChecksum(In):
  sum = 0
  In = list(In)
  if len(In) != 7:
    return "null"
  for i in range(0,7):
    if NateUtils.iseven(i):
      In[i] = int(In[i]) * 3
    else:
      In[i] = int(In[i])
  for i in range(0,7):
    sum = In[i] + sum
  nearestTen = math.ceil(sum / 10) * 10
  check = nearestTen - sum
  return check

def checkChecksum(In):
  toCheck = []
  In = list(In)
  for i in range(0,7):
    toCheck += In[i]
  if makeChecksum(toCheck) == int(In[7]):
    return True
  else:
    return False

while True:
  command = input("> ")
  command = command.lower()
  if "new|" in command:
    commandList = command.split("|")
    GTIN = commandList[1]
    name = commandList[2]
    cost = commandList[3]
    if len(GTIN) == 7:
      GTIN = GTIN + str(makeChecksum(GTIN))
    if checkChecksum(GTIN):
      f = open("products.txt","a")
      f.write(f'{GTIN}|{name}|{cost}\n')
      f.close()
      NateUtils.print_slow("Commited")
    else:
      NateUtils.print_slow("Failed GTIN Check")

  if "list|" in command:
    f = open("products.txt","r")
    for line in f.readlines():
      NateUtils.print_slow(line.strip("[']\n"))
    f.close()

  elif "gtin|" in command:
    commandList = command.split("|")
    GTIN = commandList[1]
    if len(GTIN) == 7:
      GTIN = GTIN + str(makeChecksum(GTIN))
    f = open("products.txt","r")
    for line in f.readlines():
      if GTIN in line.strip("[']\n"):
        NateUtils.print_slow(line.strip("[']\n"))
    f.close()
    
  elif "cart|" in command:
    commandList = command.split("|")
    GTIN = commandList[1]
    if len(GTIN) == 7:
      GTIN = GTIN + str(makeChecksum(GTIN))
    f = open("products.txt","r")
    for line in f.readlines():
      if GTIN in line.strip("[']\n"):
        line.strip("[']\n").split("|")
        print(line[2])
    f.close()
