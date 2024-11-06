# Jhett Carr
# UWYO COSC 1010
# Submission Date: 11/6/2024
# Lab 08
# Lab Section:15
# Sources, people worked with, help given to:
# Lecture notes
# Kaleb Moler
# Jay Trujillo
# Tutorials Point
# Stackoverflow


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

val = input("Enter a number up to one decimal point: ")


def string_inp(val):
    try:
        return int(val)
    except ValueError:
        try:
            float_val = float(val)
            if "." in val and val.count(".") == 1 and len(
                    val.split(".")[1]) <= 1:
                return float_val
            else:
                return None
        except ValueError:
            return None


print(string_inp(val))


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, upper, lower):

    if lower > upper:
        return False
    y_val = []
    x = lower
    while x <= upper:
        y = m * x + b
        y_val.append(y)
        x += 1
    return y_val


def slope_input():
    while True:
        m_input = input("Enter slope(m) or 'exit' to quit: ")
        if m_input.lower() == "exit":
            break
        b_input = input("Enter  y-intercept(b): ")
        lower_input = input("Enter lower bound: ")
        upper_input = input("Enter upper bound: ")

        try:
            m = string_inp(m_input)
            b = string_inp(b_input)
            if m is None or b is None:
                print("Invaid input, try again")
            upper = string_inp(upper_input)
            lower = string_inp(lower_input)
            if not isinstance(upper, int) or not isinstance(lower, int):
                print("Invalid, enter whole numbers")
                continue
            result = slope_intercept(m, b, upper, lower)
            if result is False:
                print(
                    "Invalid input, ensure that bounds are intergers, and that the lower bound is less than or equal to the upper bound"
                )
            else:
                print("The calculated values of y are: ", result)
        except ValueError:
            print(
                "Invalid input, ensure that bounds are integers, and that the slope and y-intercept are numbers"
            )


slope_input()

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def pos_sqrt(value):
    if value < 0:
        return None
    return value ** 0.5


def calc_quad(a, b, c):
    disc = b**2 - 4 * a * c
    if disc < 0:
        return None
    x1 = (-b + pos_sqrt(disc)) / (2 * a)
    x2 = (-b - pos_sqrt(disc)) / (2 * a)
    return x1, x2


def quad_input():
    while True:
        input_a = input("Enter value 'a' or 'exit' to quit: ")
        if input_a.lower() == "exit":
            break
        input_b = input("Enter value 'b': ")
        input_c = input("Enter value 'c': ")
        try:
            a = string_inp(input_a)
            if a is None:
                print("Invalid 'a', try again")
                continue
            b = string_inp(input_b)
            if b is None:
                print("Invalid 'b', try again")
                continue
            c = string_inp(input_c)
            if c is None:
                print("Invalid 'c', try again")
                continue
            if a == 0:
                print("Invalid, 'a' cannot be 0")
                continue
            res = calc_quad(a, b, c)
            if res is None:
                print("No real solutions")
            else:
                x1, x2 = res
                print(f"The solutions are x = {x1} and {x2}")
        except ValueError:
            print("Invalid input, ensure that only numbers are entered")


quad_input()
