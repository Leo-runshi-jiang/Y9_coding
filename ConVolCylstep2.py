print("enter in values for cylinder volume calculation")
#input 

#what inputs are needed to calculate 
#the volume of a cylinder?

# need radius and height

#radius
radius = input("\nradius in cm ")
intradius = int(radius)

#height
height = input("\nheight in cm ")
intheight = int(height)

#process

#what formula is used to calculate 
#the volume of a cylinder?

#formula: pi*r^2*h = vol of cyl

#change pi  = 3.14 to using math module

import math 

#use math

vol = math.pi * intradius * intradius * intheight

#round to 2 decimals

vol = round(vol,2)

#output

#what is important about the output?

#needs to tell vol and input info
print("\nif a cylinder has the radius of " + str(intradius) + "cm, \n\tand a height of " + str(intheight) + "cm")
print("\nit has a volume of " + str(vol) + " cm\u00b3")
print("\nequation used: volume = \u03C0 \u00d7 radius\u00b2 \u00d7 height")