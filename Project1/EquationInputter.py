import tkinter as tk
import math

def runMe():
  print("Runnning")

root = tk.Tk()

strip = tk.Label(root)
strip.config(anchor = tk.W, width = 1)
strip.pack(fill = tk.BOTH)

title = tk.Label(root, text = " Equation Input ")
#colour
title.config(fg = "white", bg = "pink")
#position (pack is a placment function)
title.pack(fill = tk.BOTH)
#radius title, W=west
strip = tk.Label(root)
strip.config(anchor = tk.W, width = 1)
strip.pack(fill = tk.BOTH)


equationLabel = tk.Label(root, text = "Equation: ")
equationLabel.config(anchor = tk.W, bg = "pink", fg = "white")
equationLabel.pack(fill = tk.BOTH)
#input box for radius
equationEntry = tk.Entry(root)
equationEntry.config()
equationEntry.pack(fill = tk.BOTH)

pinkstrip = tk.Label(root, text = "Height:")
pinkstrip.config(anchor = tk.W)
pinkstrip.pack(fill = tk.BOTH)

heightEntry = tk.Entry(root)
heightEntry.config()
heightEntry.pack(fill = tk.BOTH)
#output
output = tk.Text(root)
output.config(width = 50, height = 10, state = "disabled", borderwidth = 2, relief = "groove")
output.pack()

btnrun = tk.Button(root, text = "CALCULATE", fg = "white", highlightbackground="pink")
btnrun.config(fg="blue", command = runMe)
btnrun.pack(fill = tk.BOTH)

check = tk.Checkbutton(root, text = "High Contrast")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)
root.mainloop()