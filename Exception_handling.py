#Python uses 'except', NOT 'catch'

try:
    num = int("abc")   # This will cause an error
except ValueError:
    print("Conversion failed!")

#Output
#Conversion failed!


#What happens if we use 'catch' instead of 'except'?
#NOTE: This is just an example. Do NOT run it — it will cause a SyntaxError.

"""
try:
    num = int("abc")
catch ValueError:
    print("Error occurred")
"""

#Output
#SyntaxError: invalid syntax


#Handling Multiple Exceptions
try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero!")
except TypeError:
    print("Type error occurred!")

#Output
#Cannot divide by zero!


#try-except-else
try:
    num = 10
    print(num / 2)
except ZeroDivisionError:
    print("Error!")
else:
    print("Division successful!")

#Output
#5.0
#Division successful!


#try-except-finally
try:
    file = open("sample.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")

#Output
#File not found!
#Execution completed.


#Raising a Custom Exception
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(e)

#Output
#Age cannot be negative
