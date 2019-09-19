#declare variables
radius = 1
height = 1

#input 

#username
username = input("name: ")

while(int(radius) == 1 or intradius != 0 or intheight != 0):

	print("\nenter in values for cylinder volume calculation")

#radius
	radius = input("\nradius in cm ")
	intradius = int(radius)

#height
	height = input("\nheight in cm ")
	intheight = int(height)

#process

#calc if radius and height are +
	if (intradius >= 0 and intheight >= 0):
		import math 

		#use math

		vol = math.pi * intradius * intradius * intheight

		#round to 2 decimals

		vol = round(vol,2)

	#output

		#needs to tell vol and input info
		print("Hello there, " + username + ", I have performed your task.")
		print("\nif a cylinder has the radius of " + str(intradius) + "cm, \n\tand a height of " + str(intheight) + "cm")
		print("\nit has a volume of " + str(vol) + " cm\u00b3")
		print("\nequation used: volume = \u03C0 \u00d7 radius\u00b2 \u00d7 height")

	#else print error message
	else:
		print("Error, values cannot be less than 0.")

	print("_________________________________________________________________")
