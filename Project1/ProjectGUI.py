import tkinter as tk
from PIL import Image
from tkinter import messagebox


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
	print("Searching")
	vars = takeVars()
	print(vars)
	entry1.delete(0,tk.END) 
	entry2.delete(0,tk.END)
	entry3.delete(0,tk.END)
	entry4.delete(0,tk.END)
	entry5.delete(0,tk.END)
	processValues(vars[0],vars[1], vars[2], vars[3], vars[4])

def takeVars(*arg):
	var1 = "-1"
	var2 = "-1"
	var3 = "-1"
	var4 = "-1"
	var5 = "-1"

	#searchitems = [var1,var2,var3,var4,var5]
	searchitems = []
	#Step 2: Get all the values
	v1 = entry1.get()
	v2 = entry2.get()
	v3 = entry3.get()
	v4 = entry4.get()
	v5 = entry5.get()

	#Step 3: append to list
	searchitems.append(v1)
	searchitems.append(v2)
	searchitems.append(v3)
	searchitems.append(v4)
	searchitems.append(v5)

	return(searchitems)


def processValues(a,b,c,d,e):
	print("Processing possible formulas with " + a + ''+ b + "" + c + ""+ d +""+ e)

	# open file and read lines
	with open('form.txt', 'r') as formfile:
		formlist = formfile.readlines()

		#split and store each line as a list 
		lineone = str(formlist[0]).split(",")

		#If there is one common term, the variable for the points of that line is added by one,
		#such that the line with the most common terms will have the highest points
		line1pnt=0

		#checks for how many common terms
		if a in lineone:
			line1pnt= line1pnt+1
		if b in lineone:
			line1pnt= line1pnt+1
		if c in lineone:
			line1pnt= line1pnt+1
		if d in lineone:
			line1pnt= line1pnt+1
		if e in lineone:
			line1pnt= line1pnt+1
		
		linetwo = str(formlist[1]).split(",")
		line2pnt=0
		if a in linetwo:
			line2pnt= line2pnt+1
		if b in linetwo:
			line2pnt= line2pnt+1
		if c in linetwo:
			line2pnt= line2pnt+1
		if d in linetwo:
			line2pnt= line2pnt+1
		if e in linetwo:
			line2pnt= line2pnt+1
		
		linesix = str(formlist[5]).split(",")
		line6pnt=0
		if a in linesix:
			line6pnt= line6pnt+1
		if b in linesix:
			line6pnt= line6pnt+1
		if c in linesix:
			line6pnt= line6pnt+1
		if d in linesix:
			line6pnt= line6pnt+1
		if e in linesix:
			line6pnt= line6pnt+1
		
		lineseven = str(formlist[6]).split(",")
		line7pnt=0
		if a in lineseven:
			line7pnt= line7pnt+1
		if b in lineseven:
			line7pnt= line7pnt+1
		if c in lineseven:
			line7pnt= line7pnt+1
		if d in lineseven:
			line7pnt= line7pnt+1
		if e in lineseven:
			line7pnt= line7pnt+1
		
		#the line with the highest points gets chosen
		if line1pnt > line2pnt and line1pnt > line6pnt and line1pnt > line7pnt:
			outputimg(1)
			print("eq1")

		if line2pnt > line1pnt and line2pnt > line6pnt and line2pnt > line7pnt:
			outputimg(2)
			print("eq2")

		if line6pnt > line1pnt and line6pnt > line2pnt and line6pnt > line7pnt:
			outputimg(6)
			print("eq6")

		if line7pnt > line1pnt and line7pnt > line2pnt and line7pnt > line6pnt:
			outputimg(7)
			print("eq7")
		if line1pnt == 0 and line2pnt == 0 and line6pnt == 0 and line7pnt == 0:
			outputimg(-1)
			print("equation not found")

#the function which outputs
def outputimg(o):
	
	if o == 1:
		result = "Vf = Vi + at"
	if o == 2:
		result = "X = 1/2(Vf + Vi)t"
	if o == 6:
		result = "a" + '\u00B2'+ "+" + "b" + '\u00B2' + "=" + "c" + '\u00B2'
	if o == 7:
		result = "SinA = O/H"
	if o == -1:
		result = "Error, equation not found"
	output.config(state = "normal")
	output.delete("1.0",tk.END) #delete everything
	output.insert(tk.END,result)
	output.config(state = "disabled")




#GUI

root = tk.Tk()

root.config(bg= rootbgclr)

toolbar = tk.Label(root)
toolbar.config(bg = primeclr, width= 50)
toolbar.place(x=0, y=0)

searchbtn = tk.Button(root, text = "SEARCH", command = searchFNC)
searchbtn.config(width = 15, height = 2)
searchbtn.place(x=10,y=25)

optionlist = [
"all",
"math",
"algebric equations", 
"geometry and trig", 
"advanced functions",
"physics", 
"mechanics",
"electricity",
"waves and optics"
]

variable = tk.StringVar(root)
variable.set(optionlist[0])

searchdropdwn = tk.OptionMenu(root, variable, *optionlist)
searchdropdwn.config(width = 14, height = 2, bg = rootbgclr)
searchdropdwn.place(x=155, y=25)

entrylabel = tk.Label(root, text = "Enter Variables")
entrylabel.config(bg = primeclr, width= 33)
entrylabel.place(x=0, y=65)

#numentry is a variable that makes the rest of the widgets go down when a new widget is added above it
numentry = 5

varentryframe = tk.Frame(root)
varentryframe.config(bd = 1, bg = secondaryclr, height = 34* numentry, highlightbackground= borderclr)
varentryframe.place(x = 0, y = 95)

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
resultslabel.place(x = 0, y= 290)

resultsframe = tk.Frame(root)
resultsframe.config(bd = 1, bg = secondaryclr, height = 40, highlightbackground= borderclr)
resultsframe.place(x = 0, y = 320)

output = tk.Text(resultsframe)
output.config(width = 21, height = 1, font = ("Helvetica",24), bg = secondaryclr, state = "disabled", borderwidth = 1, highlightbackground= borderclr)
output.pack()



root.geometry("305x370+100+100")
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
