import tkinter as tk
import math

def calcVolCylinder(radius, height):

	#process

	#calc if radius and height are +
	if (radius >= 0 and height >= 0):
		vol = math.pi * radius * radius * height
		vol = round(vol,2)
		return(vol)
	else:
		return(-1)
def runMe(*args):
	print("Runnning")
	r = radiusEntry.get() 
	r = float(r)
	radiusEntry.delete(0,tk.END) 
	
	h = heightEntry.get()
	h = float(h) 
	heightEntry.delete(0,tk.END) 

	volume = calcVolCylinder(r,h)

	output.config(state = "normal")
	output.delete("1.0",tk.END)
	result = "\n\n\tr\t= "+str(r)+" units\n\th\t= "+str(h)+" units\n\tvolume\t= "+str(volume)+" units\u00B3"
	output.insert(tk.END, result)
	output.config(state = "disabled")
	print(result)

def checkSelect():
	print(var.get())

#main Program
root = tk.Tk()

title = tk.Label(root, text = "Cylinder Volume Calculator")
#colour
title.config(fg = "white", bg = "pink")
#position (pack is a placment function)
title.pack(fill = tk.BOTH)
#radius title, W=west
radiusLabel = tk.Label(root, text = "Radius:")
radiusLabel.config(anchor = tk.W)
radiusLabel.pack(fill = tk.BOTH)
#input box for radius
radiusEntry = tk.Entry(root)
radiusEntry.config()
radiusEntry.pack(fill = tk.BOTH)
#same for height
heightLabel = tk.Label(root, text = "Height:")
heightLabel.config(anchor = tk.W)
heightLabel.pack(fill = tk.BOTH)

heightEntry = tk.Entry(root)
heightEntry.config()
heightEntry.pack(fill = tk.BOTH)
#output
output = tk.Text(root)
output.config(width = 50, height = 10, state = "disabled", borderwidth = 2, relief = "groove")
output.pack()

btnrun = tk.Button(root, text = "CALCULATE", highlightbackground='#3E4149')
btnrun.config(fg="blue", command = runMe) #binds command of run me
btnrun.pack(fill = tk.BOTH)

var = tk.IntVar()


check = tk.Checkbutton(root, text = "High Contrast", variable = var, command = checkSelect)
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)


root.bind("<Return>",runMe)
root.mainloop()
print("End Program")
