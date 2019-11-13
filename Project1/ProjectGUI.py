import tkinter as tk

root = tk.Tk()

primeclr = '#F9D8D7'

toolbar = tk.Label(root)
toolbar.config(bg = primeclr, width= 50)
toolbar.grid(row = 0)

searchbtn = tk.Button(root, text = "SEARCH")
searchbtn.config(width = 30, height = 2,anchor = tk.W)
searchbtn.grid(column = 0, row = 1)

searchdropdwn = tk.Button(root)
searchdropdwn.config(width = 20, height = 2,anchor = tk.E)
searchdropdwn.grid(column = 0, row = 1)