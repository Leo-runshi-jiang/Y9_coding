data = open("randomDataRAW.txt","r")

dataString = data.read()

dataList = dataString.split("\n")



for i in range(0, len(dataList),1):
    dataList[i] = dataList[i].replace(",","")
    dataList[i] = float(dataList[i])

print (dataList)

minimum = min(dataList)
print (minimum)

smallestvalue = dataList[4]
for i in range(0, len(dataList), 1):
	if dataList[i] < smallestvalue:
		smallestvalue = dataList[i] 
print (smallestvalue)


Largestvalue = dataList[2]
for i in range(0, len(dataList),1):
	if dataList[i] > Largestvalue:
		Largestvalue = dataList[i]
print(Largestvalue)

value = input("what number do you want to set as upper limit")

sumlist=0
for i in range(0, len(dataList), 1):
	sumlist = sumlist+dataList[i]
avg = sumlist/len(dataList)
print(avg)

for i in range(0, len(tbvalues), 1):
	1stdif1 = 
	
