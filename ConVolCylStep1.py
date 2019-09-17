#input 

#what inputs are needed to calculate 
#the volume of a cylinder?

# need radius and height

#radius
radius = input("radius in cm ")
intradius = int(radius)

#height
height = input("height in cm ")
intheight = int(height)

#process

#what formula is used to calculate 
#the volume of a cylinder?

#formula: pi*r^2*h = vol of cyl

pi  = 3.14

vol = pi * intradius * intradius * intheight

#output

#what is important about the output?

#needs to tell vol 

print("The volume of the cylinder is " + str(vol) + " cm^2")
