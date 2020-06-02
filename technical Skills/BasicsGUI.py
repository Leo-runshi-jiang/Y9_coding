import tkinter as tk

print("Start Program")

def pressedbutton():
	print ("button has been pressed")
root = tk.Tk()

#create widgets
btn1 = tk.Button(root)
btn1.config(text = "Press me", width = 20, command = pressedbutton)
btn1.pack()

output = tk.Text(root)
output.pack()

outputscroll = tk.Scrollbar(output)
outputscroll.config() 
outputscroll.pack()

root.mainloop()
print("END PROGRAM")