

import tkinter as tk
from PIL import Image
from tkinter import messagebox
import json


primeclr = '#F9D8D7'
secondaryclr = '#FFFFFF'
rootbgclr = '#EFEFEF'
borderclr = '#999999'
searchitems = []
#equation1 = tk.PhotoImage(file = "vf=vi+at.png")
#When you load your program you are going to have to load all your formulas from file. 


#Functions
#Recommendation:
#Create physform.txt with a handfull of formulas
#Write teh code right below that reads the file and prints them to the screen. 
def on_closing():
	print("closing")
	if messagebox.askokcancel("quit", "Do you want to quit?"):

		root.destroy()

def searchFNC(*args):
	findEq(variable1.get(),variable2.get(),entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get())
	entry1.delete(0,tk.END) 
	entry2.delete(0,tk.END)
	entry3.delete(0,tk.END)
	entry4.delete(0,tk.END)
	entry5.delete(0,tk.END)

def findEq(subject,topic,var1,var2,var3,var4,var5):
	# open file and read lines
	file=open("Keys.txt", "r")
	equationsfile=str(file.readlines(optionlist.index(subject)))
	eqations = json.loads(equationfile)
	equationsList=equations[str(subject)][str(topic)]
	scores=[]
	unsortedScores=[]
	scoreIndex=[]
	rankedList=[]
	#store the scores of each entry in list
	#return(equationsList)
	for i in range(0,len(equationsList)):
		score=0
		if var1 in equationsList[i]:
			score=score+1
		if var2 in equationsList[i]:
			score=score+1
		if var3 in equationsList[i]:
			score=score+1
		if var4 in equationsList[i]:
			score=score+1
		if var5 in equationsList[i]:
			score=score+1
		scores.append(score)
	#get max value index
	sortedScores=scores.copy()
	sortedScores.sort(reverse=True)
	for i in range(0,len(scores)):
		for j, k in enumerate(scores):
			if k == sortedScores[i]and j not in scoreIndex:
				scoreIndex.append(j)
	
	for i in range(0,len(equationsList)):
		rankedList.append(equationsList[scoreIndex[i]][0])


	string=" ".join(rankedList)
	output(string)

#the function which outputs
def output(List):
	outputbox.config(state = "normal")
	outputbox.delete("1.0",tk.END) #delete everything
	outputbox.insert(tk.END,List)
	outputbox.config(state = "disabled")




#GUI

root = tk.Tk()

root.config(bg= rootbgclr)

toolbar = tk.Label(root)
toolbar.config(bg = primeclr, width= 50)
toolbar.place(x=0, y=0)

searchbtn = tk.Button(root, text = "SEARCH", command = searchFNC)
searchbtn.config(width = 15, height = 3)
searchbtn.place(x=10,y=25)

optionlist = [
"All",
"Math",
"Physics",
"Chems"
]

secondlist= [
"All",
"Kinematics",
"Mechanics"]

variable1 = tk.StringVar(root)
variable1.set(optionlist[0])

variable2 = tk.StringVar(root)
variable2.set(secondlist[0])

searchdropdwn = tk.OptionMenu(root, variable1, *optionlist)
searchdropdwn.config(width = 14, height = 2, bg = rootbgclr)
searchdropdwn.place(x=155, y=20)

searchdropdwn = tk.OptionMenu(root, variable2, *secondlist)
searchdropdwn.config(width = 14, height = 2, bg = rootbgclr)
searchdropdwn.place(x=155, y=50)

entrylabel = tk.Label(root, text = "Enter Variables")
entrylabel.config(bg = primeclr, width= 33)
entrylabel.place(x=0, y=85)

#numentry is a variable that makes the rest of the widgets go down when a new widget is added above it
numentry = 5

varentryframe = tk.Frame(root)
varentryframe.config(bd = 1, bg = secondaryclr, height = 34* numentry, highlightbackground= borderclr)
varentryframe.place(x = 0, y = 115)

entry1 = tk.Entry(varentryframe)
entry1.config(width = 21, font = ("Helvetica",24), bg = secondaryclr, borderwidth=0.25, highlightbackground = borderclr)
entry1.pack()

entry2 = tk.Entry(varentryframe)
entry2.config(width = 21, font = ("Helvetica",24), bg = secondaryclr, borderwidth=0.25, highlightbackground = borderclr)
entry2.pack()

entry3 = tk.Entry(varentryframe)
entry3.config(width = 21,  font = ("Helvetica",24), bg = secondaryclr, borderwidth=0.25, highlightbackground = borderclr)
entry3.pack()

entry4 = tk.Entry(varentryframe)
entry4.config(width = 21, font = ("Helvetica",24), bg = secondaryclr, borderwidth=0.25, highlightbackground = borderclr)
entry4.pack()

entry5 = tk.Entry(varentryframe)
entry5.config(width = 21, font = ("Helvetica",24), bg = secondaryclr, borderwidth=0.25, highlightbackground = borderclr)
entry5.pack()

resultslabel = tk.Label(root, text = "Results")
resultslabel.config(bg = primeclr, width= 33)
resultslabel.place(x = 0, y= 300)

resultsframe = tk.Frame(root)
resultsframe.config(bd = 1, bg = secondaryclr, height = 40, highlightbackground= borderclr)
resultsframe.place(x = 0, y = 320)

outputbox = tk.Text(resultsframe)
outputbox.config(width = 21, height = 3, font = ("Helvetica",24), bg = secondaryclr, state = "disabled", borderwidth = 1, highlightbackground= borderclr)
outputbox.pack()



root.geometry("305x400+100+100")
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()