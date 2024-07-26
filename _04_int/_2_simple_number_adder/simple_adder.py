"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # Ask the user for the first number

    num1 = simpledialog.askinteger(title="Adder", prompt="Enter the first number: ")


    # Ask the user for the second number
    num2 = simpledialog.askinteger(title="Adder", prompt="Enter the second number: ")
    #num2 = float(input("Enter the second number: "))

    # Calculate the sum of the two numbers
    sum_of_numbers = num1 + num2

    # Display the sum to the user
    messagebox.showinfo(title="Adder", message=sum_of_numbers)



