"""
Modules and Packages in Python:
- what is a module
- importing a module
- import with alias
- from module import specific function
- built-in modules (math, random, datetime)
- __name__ == "__main__"
"""

# -------------------------------
# IMPORTING A BUILT-IN MODULE
# -------------------------------
import math

print("Square Root of 16:", math.sqrt(16))
print("Value of Pi:", math.pi)

# Output
# Square Root of 16: 4.0
# Value of Pi: 3.141592653589793


# -------------------------------
# IMPORT WITH ALIAS
# -------------------------------
import random as rd

print("Random Number (1-10):", rd.randint(1, 10))

# Output
# Random Number (1-10): (any number between 1 and 10)


# -------------------------------
# FROM MODULE IMPORT FUNCTION
# -------------------------------
from datetime import date

today = date.today()
print("Today's Date:", today)

# Output
# Today's Date: YYYY-MM-DD


# -------------------------------
# CREATING YOUR OWN MODULE
# (Imagine this is in another file named mymodule.py)
# -------------------------------

# mymodule.py
def multiply(a, b):
    return a * b


# -------------------------------
# USING YOUR OWN MODULE
# (In main file)
# -------------------------------

# import mymodule
# result = mymodule.multiply(5, 4)
# print("Multiplication Result:", result)

# Output
# Multiplication Result: 20


# -------------------------------
# __name__ == "__main__"
# -------------------------------
def main():
    print("This runs only if file is executed directly")

if __name__ == "__main__":
    main()

# Output
# This runs only if file is executed directly

