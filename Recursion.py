"""
RECURSION – EXAMPLES
"""


# -----------------------------
# 1️⃣ Factorial using Recursion
# -----------------------------

def factorial(n):
    if n == 0 or n == 1:   # Base Case
        return 1
    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))

#Output
#Factorial of 5: 120


# -----------------------------
# 2️⃣ Fibonacci using Recursion
# -----------------------------

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci of 6:", fibonacci(6))

#Output
#Fibonacci of 6: 8


# -----------------------------
# 3️⃣ Sum of Natural Numbers
# -----------------------------

def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


print("Sum up to 5:", sum_numbers(5))

#Output
#Sum up to 5: 15

