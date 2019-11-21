import tkinter as tk

primeclr = '#F9D8D7'
secondaryclr = '#FFFFFF'
rootbgclr = '#EFEFEF'
borderclr = '#999999'

root = tk.Tk()

root.config(bg= rootbgclr)

toolbar = tk.Label(root)
toolbar.config(bg = primeclr, width= 50)
toolbar.place(x=0, y=0)

searchbtn = tk.Button(root, text = "SEARCH")
searchbtn.config(width = 15, height = 2)
searchbtn.place(x=25,y=25)

optionlist = [
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
searchdropdwn.config(width = 10, height = 2, bg = rootbgclr)
searchdropdwn.place(x=175, y=25)

entrylabel = tk.Label(root, text = "Enter Variables")
entrylabel.config(bg = primeclr, width= 33)
entrylabel.place(x=0, y=65)

#numentry is a variable that makes the rest of the widgets go down when a new widget is added above it
numentry = 5
numreturn = 3

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
resultsframe.config(bd = 1, bg = secondaryclr, height = 17 * numreturn, highlightbackground= borderclr)
resultsframe.place(x = 0, y = 320)

return1 = tk.Text(resultsframe)
return1.config(width = 41, height = 2, bg = secondaryclr, state = "disabled", borderwidth = 1, highlightbackground= borderclr)
return1.pack()

return2 = tk.Text(resultsframe)
return2.config(width = 41, height = 2, bg = secondaryclr, state = "disabled", borderwidth = 1, highlightbackground= borderclr)
return2.pack()

return3 = tk.Text(resultsframe)
return3.config(width = 41, height = 2, bg = secondaryclr, state = "disabled", borderwidth = 1, highlightbackground= borderclr)
return3.pack()

root.geometry("305x700+100+100")
root.mainloop()
