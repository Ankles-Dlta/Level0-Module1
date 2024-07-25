from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
name = simpledialog.askstring(title="Tomato colors", prompt="Do you want red tomatos, brown tomatos, or black tomatos")

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if name == 'red':
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")

elif name == 'brown':
    canvas.create_oval(75, 200, 400, 450, fill="tan", outline="black")
    canvas.create_oval(200, 200, 525, 450, fill="tan", outline="black")
    canvas.create_rectangle(275, 100, 325, 230, fill="tan", outline="black")


else:
    canvas.create_oval(75, 200, 400, 450, fill="black", outline="black")
    canvas.create_oval(200, 200, 525, 450, fill="black", outline="black")
    canvas.create_rectangle(275, 100, 325, 230, fill="grey", outline="black")

    messagebox.showinfo("wrong")
root.mainloop()
