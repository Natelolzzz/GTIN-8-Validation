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
  
GTIN = input("> ")
if len(GTIN) == 7:
    print(makeChecksum(GTIN))
if len(GTIN) == 8:
    print(checkChecksum(GTIN))
