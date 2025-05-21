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

cost = 0
cart = []

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
      f.write(f"{GTIN}|{name}|{cost}\n")
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
    
  elif "clearcart|" in command:
    cart = []
    cost = 0
    
  elif "listcart|" in command:
    for i in range(len(cart)):
      f = open("products.txt","r")
      for line in f.readlines():
        if cart[i][0] in line.strip("[']\n"):
          line = line.strip("[']\n")
          line += "|"
          line += str(cart[i][1])
          NateUtils.print_slow(line)
      f.close()
  
  elif "cart|" in command:
    commandList = command.split("|")
    GTIN = commandList[1]
    if len(commandList) > 2:
      times = int(commandList[2])
    else: 
      times = 1
    if len(GTIN) == 7:
      GTIN = GTIN + str(makeChecksum(GTIN))
    f = open("products.txt","r")
    for line in f.readlines():
      if GTIN in line.strip("[']\n"):
        line = line.strip("[']\n")
        line = line.split("|")
        found = False
        for i in range(len(cart)):
          if GTIN in cart[i][0]:
            cart[i][1] = str(int(cart[i][1]) + times)
            cost += float(line[2])*times
            found = True
        if found == False:    
          cost += float(line[2])*times
          cart.append([GTIN,times])
        NateUtils.print_slow("Found a match, added to cart")
    f.close()
  
  elif "checkout|" in command:
    commandList = command.split("|")
    for i in range(len(cart)):
      f = open("products.txt","r")
      for line in f.readlines():
        if cart[i][0] in line.strip("[']\n"):
          line = line.strip("[']\n")
          line += "|"
          line += str(cart[i][1])
          NateUtils.print_slow(line)
      f.close()
    NateUtils.print_slow(f"Your total is {cost}, thank you for coming!")
    cart = []
    cost = 0
