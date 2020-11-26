import tkinter as tk
import requests

def runMe(*args):
	#get number
	num=numberEntry.get()
	#contact api
	url = "http://numbersapi.com/"+str(num)
	response = requests.get(url)
	print (response.text)
	#clear entry
	numberEntry.delete(0, tk.END)

	output.config(state = "normal")
	output.delete("1.0",tk.END)
	output.insert(tk.END, response.text)
	output.config(state = "disabled")


root = tk.Tk()

title = tk.Label(root, text = "Number facts finder")
#colour
title.config(fg = "white", bg = "blue")
#position (pack is a placment function)
title.pack(fill = tk.BOTH)
#radius title, W=west
numberLabel = tk.Label(root, text = "Number:")
numberLabel.config(anchor = tk.W)
numberLabel.pack(fill = tk.BOTH)
#input box for radius
numberEntry = tk.Entry(root)
numberEntry.config()
numberEntry.pack(fill = tk.BOTH)
#output
output = tk.Text(root)
output.config(width = 50, height = 4, state = "disabled", borderwidth = 2, relief = "groove")
output.pack()

btnrun = tk.Button(root, text = "Get Answer", highlightbackground='white')
btnrun.config(fg="blue", command = runMe) #binds command of run me
btnrun.pack(fill = tk.BOTH)

root.mainloop()