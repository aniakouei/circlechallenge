#import math
#create class for circle
    # create function to initialize and set radius property
    # create function to calculate diameter
    #create function to calculate circumference
    #create a function to calculate are
    #create a function that doubles the radius
    #create a function that returns the radius value
#create a function to print the valid radius
    # create a loop with an if statement to make sure the user input is a positive radius
#create a function for the main
    #create a while loop that prints the circle information
    # ask user input if they would like the circle to grow
    #create if statement if yes to call grow function and loop again and if no it breaks
#call main function to run through program
    


import math

class Circle:
    def __init__(self, radius):
        self.radius=radius

    def calcuate_diameter(self):
      return 2 * self.radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def grow(self):
        self.radius *=2

    def get_radius(self):
        return self.radius

def valid_radius():
    while True:
        radius=float(input("Enter a Radius: "))
        if radius>0:
            return radius
        else:
            print("Please enter a positive number")

def main():
    radius=valid_radius()
    circle=Circle(radius)

    while True:
        print("Circle Information")
        print(f"Diameter: {circle.calcuate_diameter()}")
        print(f"Circumference: {circle.calculate_circumference()}")
        print(f"Area: {circle.calculate_area()}")

        grows=input("Would you like your circle to grow? (yes/no): ").lower()
        if grows=="yes":
            circle.grow()
        elif grows=="no":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter 'yes' or 'no'.")
main()

