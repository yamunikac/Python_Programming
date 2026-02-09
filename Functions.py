"""
Functions in Python:
- defining a function
- parameters and arguments
- return statement
- default parameters
- keyword arguments
- arbitrary arguments (*args, **kwargs)
- lambda functions
- recursion
"""


# -------------------------------
# BASIC FUNCTION
# -------------------------------
def greet():
    print("Hello Yamunika, Welcome to Python!")
greet()
#Output
#Hello Yamunika, Welcome to Python!


# -------------------------------
# FUNCTION WITH PARAMETERS
# -------------------------------
def greet_user(name):
    print("Hello", name, "- Keep learning and building!")
greet_user("Yamunika")
#Output
#Hello Yamunika - Keep learning and building!


# -------------------------------
# FUNCTION WITH RETURN VALUE
# -------------------------------
def add_marks(maths, science):
    return maths + science
total = add_marks(85, 90)
print("Total Marks:", total)
#Output
#Total Marks: 175



# -------------------------------
# DEFAULT PARAMETERS
# -------------------------------
def course(track="Python Full Stack"):
    print("Current Learning Track:", track)
course("Web Development")
course()
#Output
#Current Learning Track: Web Development
#Current Learning Track: Python Full Stack



# -------------------------------
# KEYWORD ARGUMENTS
# -------------------------------
def student_details(name, age):
    print("Student Name:", name)
    print("Age:", age)
student_details(name="Yamunika", age=20)
#Output
#Student Name: Yamunika
#Age: 20


# -------------------------------
# ARBITRARY ARGUMENTS (*args)
# Allows multiple marks
# -------------------------------
def total_scores(*marks):
    print("Total Score:", sum(marks))
total_scores(88, 92, 79, 85)
#Output
#Total Score: 344


# -------------------------------
# ARBITRARY KEYWORD ARGUMENTS (**kwargs)
# Student profile example
# -------------------------------
def profile(**info):
    for key, value in info.items():
        print(key, ":", value)
profile(name="Yamunika", role="Aspiring Developer", goal="Full Stack Engineer")
#Output
#name : Yamunika
#role : Aspiring Developer
#goal : Full Stack Engineer


# -------------------------------
# LAMBDA FUNCTION
# -------------------------------
square = lambda x: x * x
print("Square of 6:", square(6))
#Output
#Square of 6: 36


# -------------------------------
# RECURSION
# Factorial example
# -------------------------------
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print("Factorial of 5:", factorial(5))
#Output
#Factorial of 5: 120
