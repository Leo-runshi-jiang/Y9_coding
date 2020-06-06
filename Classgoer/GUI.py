#problems: create widget doesnt work in for loop
#cannot get from entry on edit window



import tkinter as tk
from datetime import datetime
import sys
import time
import webbrowser

frames = []
widgets = []
'''
the files txt files used are in a format there it goes
"object,data associated with object,object2"

ex: "science, link to science class, history, link to history class"
this so the txt can be converted to a list and allow other functions 
to read/manipulate the file
'''

#functions used to read/convert/delete files of this format

#turns file into list
def turntolist(filename):
	file=open(filename, "r")
	filestring = file.read()
	return filestring.split(",")

#delete the article and the value
def deletelistitem(file,delarticlename):
	listfile=turntolist("ClassLinks.txt")
	articlelist=listfile[::2]
	delitemindex=articlelist.index(delarticlename)*2
	listfile.pop(delitemindex)
	listfile.pop(delitemindex)
	rewritefile=open(file, "w")
	for i in range(0,len(listfile)-1,1):
		rewritefile.write(listfile[i]+",")

#delete the value
def deletelistvalue(file,delarticlename):
	listfile=turntolist("ClassLinks.txt")
	articlelist=listfile[::2]
	delitemindex=articlelist.index(delarticlename)*2
	listfile.pop(delitemindex+1)
	rewritefile=open(file, "w")
	for i in range(0,len(listfile)-1,1):
		rewritefile.write(listfile[i]+",")

def readvalue(listname,article):
	valueindex=listname.index(article)
	return listname[valueindex+1]

#functional bits

#this function returns the link to the class
def findlink(classname):
	listclass = turntolist("ClassLinks.txt")
	classnamelist=listclass[::2]
	#the slice here removes all odd indexes,
	#leaving only class names, removing links
	if classname in classnamelist:
		classindex=classnamelist.index(classname)
		linkindex= classindex*2+1
		print(linkindex)
		#finds class in list of classes,
		#then doubles and +1 to find index of link to class
		return listclass[linkindex]
	else:
		return "class not found"

#this function opens the browser
def gotoclass(inputclass):
	openclasslink = findlink(inputclass)
	webbrowser.open(openclasslink)

#this creates more widgets for when there are moew classes added

def createclasswidgets(name,number):
	#reads value of num class
	#lenclasslist=len(turntolist("ClassLinks.txt"))-1
	#numclass=lenclasslist/2
	classlabel = tk.Label(classframe,width=15,font=("Helvetica", 20),text=name)
	classbtn= tk.Button(classframe,width=10,relief="flat",text="Go to class",command=lambda: gotoclass(name))
	classbtn.config(fg="#4A86E8")
	widgets.append(classframe)
	modnumber=number%2
	if number != 0:
		rownumber=((number-modnumber)/2)
	else:
		rownumber=0
	if int(modnumber) == 0:
		classlabel.grid(row=int(rownumber),column=0)
		classbtn.grid(row=int(rownumber),column=1)
	else:
		classlabel.grid(row=int(rownumber),column=3)
		classbtn.grid(row=int(rownumber),column=4)

#loads all the classes, this runs everytime the root window is ran
def loadclasses():
	listclass=turntolist("ClassLinks.txt")
	classnamelist=listclass[::2]
	for i in range(0,len(classnamelist)-1,1):
		print(i)
		createclasswidgets(classnamelist[0],1)

#GUI specific functions
def getdate():
	now = datetime.now()

	current_time = now.strftime("%A"+", "+"%m" + "/"+"%d")
	return current_time

def tickingclock():
    time_string = time.strftime("%H:%M")
    clock.config(text=time_string)
    clock.after(1000, tickingclock)

#other windows
def editwindow():
    editwindow = tk.Toplevel(root)

    divider3 = tk.Label(editwindow)
    divider3.config(bg="#4A86E8", height=1)
    divider3.pack(fill="both")

    divider4 = tk.Label(editwindow, text="Enter in Class name and Link to class", font=("Helvetica", 20))
    divider4.pack(fill="both")

    divider5 = tk.Label(editwindow)
    divider5.config(bg="#4A86E8", height=1)
    divider5.pack(fill="both")

    addorchangeframe=tk.Frame(editwindow, bg="#EDEDED")
    addorchangeframe.pack()

    classnameentry=tk.Entry(addorchangeframe)
    classnameentry.grid(column=1,row=0)

    addorchangebtn=tk.Button(addorchangeframe,text="Add or change",command=addorchange)
    addorchangebtn.grid(column=2,row=0)

    classlinkentry=tk.Entry(addorchangeframe)
    classlinkentry.grid(column=1,row=2)


#def editclass():

def addorchange():
	newclassname=classnameentry.get()
	print(newclassname)
	newclasslink=classlinkentry.get()
	print(newclasslink)
	listclass=turntolist("ClassLinks.txt")
	classnamelist=listclass[::2]
	if newclassname in classnamelist:
		delclassindex=classnamelist.index(newclassname)*2
		listclass.pop(delclassindex)
		listclass.pop(delclassindex)
	#now the class and the link is deleted from the list,
	#rewrtie the file with the current list
		rewritefile=open("ClassLinks.txt", "w")
		for i in range(0,len(listclass)-1,1):
			rewritefile.write(listclass[i]+",")
		appendclassfile=open("ClassLinks.txt", "a")
		appendclassfile.write(newclassname+","+newclasslink+",")
		print("class edited")
	else:
		appendclassfile=open("ClassLinks.txt", "a")
		appendclassfile.write(newclassname+","+newclasslink+",")
		print("class added")

	loadclasses()



def addclass(newclassname,newclasslink):
	listclass=turntolist("ClassLinks.txt")
	if newclassname in listclass:
		print("class already added")
	else:
		appendclassfile=open("ClassLinks.txt", "a")
		appendclassfile.write(newclassname+","+newclasslink+",")
		print("class added")

def deleteclass(delclassname):
	#go to class names, search for name to delete, delete it and the link after it
	listclass=turntolist("ClassLinks.txt")
	classnamelist=listclass[::2]
	delclassindex=classnamelist.index(delclassname)*2
	listclass.pop(delclassindex)
	listclass.pop(delclassindex)
	#now the class and the link is deleted from the list,
	#rewrtie the file with the current list
	rewritefile=open("ClassLinks.txt", "w")
	for i in range(0,len(listclass)-1,1):
		rewritefile.write(listclass[i]+",")


def editclassframe():
	#DESTROYS original frame, create new one and loads all again
	classframe.destroy()
	classframe = tk.Frame(parentframe, borderwidth=2, relief="groove")
	frames.append(classframe)
	classframe.pack()
	loadclasses()


root = tk.Tk()
root.config(bg="#EDEDED")

clockiconpng = tk.PhotoImage(file="Images/clockicon.png")
peniconpng = tk.PhotoImage(file="Images/editpenicon.png")
schedule=tk.PhotoImage(file="Images/schedule.png")
topframe = tk.Frame(root)
topframe.pack()

date = tk.Label(topframe, text = getdate(), font=("Helvetica", 50))
date.config(fg="white", bg="#4A86E8",anchor="w",width=15, padx=20)
date.grid(row=0, column=0)

clockicon = tk.Label(topframe,image=clockiconpng)
clockicon.config(bg="white")
clockicon.grid(row=0, column=1)

clock = tk.Label(topframe,font=("Helvetica", 50))
clock.config(fg="black", bg="white", anchor="w")
clock.grid(row=0, column=2)
tickingclock()

editclassbtn =tk.Button(root, text="Edit classes", image= peniconpng,compound="left",command=editwindow, font=("Helvetica", 14))
editclassbtn.config(width=15)
editclassbtn.pack(anchor="w",padx=20)

divider1 = tk.Label(root)
divider1.config(bg="#4A86E8", height=1)
divider1.pack(fill="both")

parentframe=tk.Frame(root)
parentframe.pack()
classframe = tk.Frame(parentframe, borderwidth=2, relief="groove")
frames.append(classframe)

classframe.pack()

divider2 = tk.Label(root)
divider2.config(bg="#4A86E8", height=1)
divider2.pack(fill="both")

scheduleimg=tk.Label(root, image=schedule, width=650)
scheduleimg.pack()

loadclasses()
root.mainloop()
