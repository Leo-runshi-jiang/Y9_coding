
def getWholeNumAndFraction(numerator,denominator):
	remainder = numerator%denominator
	wholenum = (numerator-remainder)/denominator
	return([int(wholenum),remainder,denominator])

def findGCF(numerator,denominator):

	result = False

	while result == False:
		if numerator > denominator:
			numerator = numerator-denominator

		if numerator < denominator:
			denominator = denominator-numerator

		if numerator == denominator:
			result = True
			return numerator

def simplifyFraction(numerator,denominator):
	GCF = findGCF(numerator,denominator)
	return([int(numerator/GCF),int(denominator/GCF)])


def getAnswer():
	numerator = int(input("numerator"))
	denominator = int(input("denom"))

	if getWholeNumAndFraction(numerator,denominator)[1]==0:
		print(str(getWholeNumAndFraction(numerator,denominator)[0]))

	elif getWholeNumAndFraction(numerator,denominator)[0]==0:
		new_numerator = simplifyFraction(getWholeNumAndFraction(numerator,denominator)[1],getWholeNumAndFraction(numerator,denominator)[2])[0]
		new_denominator = simplifyFraction(getWholeNumAndFraction(numerator,denominator)[1],getWholeNumAndFraction(numerator,denominator)[2])[1]

		print(str(new_numerator)+"/" +str(new_denominator))

	else:
		new_numerator = simplifyFraction(getWholeNumAndFraction(numerator,denominator)[1],getWholeNumAndFraction(numerator,denominator)[2])[0]
		new_denominator = simplifyFraction(getWholeNumAndFraction(numerator,denominator)[1],getWholeNumAndFraction(numerator,denominator)[2])[1]

		print(str(getWholeNumAndFraction(numerator,denominator)[0])+" "+str(new_numerator)+"/" +str(new_denominator))

while(True):
	getAnswer()
	
