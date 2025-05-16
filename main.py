import math

def iseven(num):
  if num % 2:
      return False
  else:
      return True

def makeChecksum(In):
  sum = 0
  In = list(In)
  if len(In) != 7:
    return "null"
  for i in range(0,7):
    if iseven(i):
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
    cost = float(commandList[3])
    if len(GTIN) == 7:
      GTIN = int(GTIN + str(makeChecksum(GTIN)))
    if checkChecksum(str(GTIN)) //todo

      print("Commited")
    else:
      print("Failed GTIN Check")
  if "list|" in command:
//todo
    for i in ans:
      print(i)
  if "gtin|" in command:
    GTIN = int(commandList[1])
  //todo
