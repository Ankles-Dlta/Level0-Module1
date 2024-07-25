import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.
a
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    bob = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    name = simpledialog.askstring(title="Shapes", prompt="What shape do you want to draw (circle, square or triangle")
    # Draw the shape requested by the user using if-elif-else statements
    if name == 'circle':
        bob.penup()
        bob.circle(radius)


    # Call the turtle .done() method
