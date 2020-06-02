from tkinter import *
from random import randint

def moveball()
	deltx=1
	delty=1
	canvas.move(ball1,deltx,delty)
	root.after(100,moveball)
root = tk()
root.title("moving balls")
root.resizable(false,falses)

canvas = Canvas(root,width = 300, height=300)
canvas.pack()

ball1=canvas.creatoval(10,10,20,20,fill="red")
ball2=canvas.creatoval(30,30,40,40,fill="red")

root.after(100,moveball)
root.mainloop()