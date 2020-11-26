#find perfect numbers between 2-1000
import math
def factor(a):
	factorlist=[]
	
	for i in range(1,int(math.sqrt(a))+1,1):
		if a%i ==0:
			factorlist.append(int(i))
			if i !=1:
				factorlist.append(int(a/i))		
	return(factorlist)
def addfactors(factors):
	sum=0
	for i in range(0,len(factors),1):
		sum=sum+factors[i]
	return(sum)
def checknumber(min,max):
	answers=[]
	for i in range(min,max,1):
		sumfactors=addfactors(factor(i))
		if sumfactors == i:
			answers.append(i)
	return(answers)
print(checknumber(2,1000))
#print(factor(28))


