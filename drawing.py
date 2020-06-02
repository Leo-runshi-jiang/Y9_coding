import tkinter as tk
root = tk.Tk()

canvas = tk.Canvas(root, width=220, height=400)
canvas.pack()
canvas.create_polygon(10,200,10,210,210,210,210,200)
canvas.create_polygon(50,190,85,125,110,140,135,125,170,190)
canvas.create_oval(40, 290, 100,230)
canvas.create_oval(120, 290, 180,230)
canvas.create_oval(70, 260, 70,260)
canvas.create_oval(150, 260, 150,260)
canvas.create_oval(70, 370, 170,300)
root.mainloop()
