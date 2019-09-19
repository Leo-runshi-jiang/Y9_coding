import math

def calcVolCylinder(radius, height):

	#process

	#calc if radius and height are +
	if (radius >= 0 and height >= 0):

		#use math

		vol = math.pi * radius * radius * height

		#round to 2 decimals

		vol = round(vol,2)

	#output

		return(vol)

	#else print error message
	else:
		return(-1)

#main Program
print("Start Program")
result = (calcVolCylinder(-4,3))
print(result)
print("End Program")
