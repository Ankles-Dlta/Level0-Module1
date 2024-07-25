# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
import math


def main():
    # Ask the user for the radius of the circle
    radius = float(input("Enter the radius of the circle: "))

    # Ask the user whether they want to calculate area or circumference
    choice = input(
        "Would you like to calculate the area or circumference? (Enter 'area' or 'circumference'): ").strip().lower()

    if choice == 'area':
        # Calculate the area of the circle
        area = math.pi * radius ** 2
        print(f"The area of the circle with radius {radius} is {area:.2f}")
    elif choice == 'circumference':
        # Calculate the circumference of the circle
        circumference = 2 * math.pi * radius
        print(f"The circumference of the circle with radius {radius} is {circumference:.2f}")
    else:
        print("Invalid choice. Please enter 'area' or 'circumference'.")


if __name__ == "__main__":
    main()
