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
def runMe():
  print("Runnning")
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
btnrun.config(fg="blue")
btnrun.pack(fill = tk.BOTH)

check = tk.Checkbutton(root, text = "High Contrast")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)
root.mainloop()
print("End Program")
