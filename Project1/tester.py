import tkinter as tk      
root = tk.Tk()      
canvas = tk.Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = tk.PhotoImage(file="quack men square.png")      
canvas.create_image(20,20, image=img)      
mainloop()
