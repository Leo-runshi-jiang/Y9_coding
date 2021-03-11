import tkinter as tk
import random
from tkinter import ttk

var runtimes=False

def getplayerIDs():
	return("1111111","22222222")

def get_playertag(*args):
	print(IDchoosen.get())
	if runtimes==True:
		divider1.destroy()
	divider1 = tk.Label(root)
	divider1.config(bg="#434343", height=1, width= 100)
	divider1.pack(fill="both")
	runtimes=True


root = tk.Tk()
combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'fieldbackground': 'white',
                                       'background': 'white'
                                       }}}
                         )
combostyle.theme_use('combostyle')

n = tk.StringVar() 
IDchoosen = ttk.Combobox(root, width = 10, height = 10, textvariable = n, font=("Helvetica", 30)) 
IDchoosen['values'] = getplayerIDs()
IDchoosen.pack()

search = ttk.Button(root, text = "Search")
search.config(command=get_playertag)
search.pack()

root.mainloop()