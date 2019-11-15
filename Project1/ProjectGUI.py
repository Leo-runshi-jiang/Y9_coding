import tkinter as tk

root = tk.Tk()

primeclr = '#F9D8D7'

toolbar = tk.Label(root)
toolbar.config(bg = primeclr, width= 50)
toolbar.place(x=0, y=0)

searchbtn = tk.Button(root, text = "SEARCH")
searchbtn.config(width = 20, height = 2)
searchbtn.place(x=25,y=25)

searchdropdwn = tk.Button(root)
searchdropdwn.config(width = 15, height = 2)
searchdropdwn.place(x=225, y=25)

entrylabel = tk.Label(root, text = "Enter in variables")
entrylabel.config(bg = primeclr, width= 50)
entrylabel.place(x= -20, y=65)

entry1label = tk.Label(root, text = "  Variable 1")
entry1label.config(width= 50, anchor=tk.W)
entry1label.place(x=0, y=85)

entry1 = tk.Entry(root)
entry1.config(width = 40)
entry1.place(x=5, y=115)

root.geometry("400x700+100+100")
root.mainloop()
