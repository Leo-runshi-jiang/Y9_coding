import tkinter as tk

text = "1,vx0,ax,t"

list = text.split(",");
print(list)



#When you load your program you are going to have to load all your formulas from file. 


#Functions
#Recommendation:
#Create physform.txt with a handfull of formulas
#Write teh code right below that reads the file and prints them to the screen. 


def processValues(a,b,c,d,e):
	print("Processing possible formulas")



def searchFNC(*args):
	print("BUTTON PRESSED")

	#Question: What are the conditions around what is in the entry

	
	#step 1: 
	#I assume all values are invalid
	check = [False,False,False,False,False]

	#Step 2: Get all the values
	v1 = entry1.get()
	v2 = entry2.get()
	v3 = entry3.get()
	v4 = entry4.get()
	v5 = entry5.get()

	#Step 3: try to cast to an int and if that fails we know it is valid
	try:
		v1 = int(v1) #If this is an in!!!
		
	except:
		print("It is a letter")
		check[0] = True


	try:
		v2 = int(v2) #If this is an in!!!
		
	except:
		print("It is a letter")
		check[1] = True

	try:
		v3 = int(v3) #If this is an in!!!
		
	except:
		print("It is a letter")
		check[2] = True

	try:
		v4 = int(v4) #If this is an in!!!
		
	except:
		print("It is a letter")
		check[3] = True

	try:
		v5 = int(v5) #If this is an in!!!
		
	except:
		print("It is a letter")
		check[4] = True


	runprocess = True

	for i in range(0,len(check),1):
		if (check[i] == False):
			runprocess = False

	if runprocess == True:
		processValues(v1,v2,v3,v4,v5)

