numbers = [63,59,34,19,13,12,11,10,9,9,9,8,7,7,6,6,6,5,4,4,4,4,4,3,3,2,2,1,1,1,1,1,1,1,1]
string = ""
index=0
sums=0
for i in range(0,len(numbers)):
	term = str(numbers[i])+"("+str(numbers[i])+"-"+"1"+")"+"+"
	string= string+str(term)
print(string)

for i in range(0,len(numbers)):
	sums=numbers[i]+sums
	index = index+numbers[i]*(numbers[i]-1)
print(sums)
print(index)
print(sums*(sums-1)/index)