"""
PYTHON STANDARD LIBRARIES – BASIC DEMONSTRATION
"""

import math
import random
import datetime
import os
from collections import Counter


# -----------------------------
# 1️⃣ math Module
# -----------------------------

print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)


# -----------------------------
# 2️⃣ random Module
# -----------------------------

print("Random number (1-10):", random.randint(1, 10))


# -----------------------------
# 3️⃣ datetime Module
# -----------------------------

now = datetime.datetime.now()
print("Current Date and Time:", now)


# -----------------------------
# 4️⃣ os Module
# -----------------------------

print("Current Working Directory:", os.getcwd())


# -----------------------------
# 5️⃣ collections Module
# -----------------------------

data = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(data)

print("Item Frequency:", count)

#Example Output (will vary for random & datetime):
#Square root of 25: 5.0
#Value of pi: 3.141592653589793
#Random number (1-10): 7
#Current Date and Time: 2026-02-22 18:45:00
#Current Working Directory: /your/path
#Item Frequency: Counter({'apple': 3, 'banana': 2, 'orange': 1})
