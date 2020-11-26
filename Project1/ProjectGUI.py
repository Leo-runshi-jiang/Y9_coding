import tkinter as tk

def getentry():
	entry=entry1.get()
	print(entry)
root = tk.Tk()


entry1 = tk.Entry(root)
entry1.pack()

editclassbtn =tk.Button(root, text="Edit classes",command=getentry, font=("Helvetica", 14))
editclassbtn.config(width=15)
editclassbtn.pack(anchor="w",padx=20)
root.mainloop()
