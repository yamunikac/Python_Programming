"""
LAMBDA, MAP, FILTER, REDUCE – COMPLETE BASIC DEMONSTRATION
"""

from functools import reduce


# -----------------------------
# 1️⃣ Lambda Function
# -----------------------------

square = lambda x: x * x
print("Square of 5:", square(5))

#Output
#Square of 5: 25


# -----------------------------
# 2️⃣ map() Function
# -----------------------------

numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))
print("Squares using map:", squares)

#Output
#[1, 4, 9, 16]


# -----------------------------
# 3️⃣ filter() Function
# -----------------------------

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#Output
#[2, 4]


# -----------------------------
# 4️⃣ reduce() Function
# -----------------------------

product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)

#Output
#24
