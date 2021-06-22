numer = int(input("Enter Numerator"))
denom = int(input("Enter Denominator"))

newNumer = numer%denom
mixedNum = numer/denom

if(numer ==0):
	print("0")

elif (mixedNum == 0):
	print(str(numer)+"/"+str(denom))

elif (newNumer ==0):
	print(str(mixedNum))

else: 
	print(str(mixedNum)+""+str(newNumer)+"/"+str(denom))