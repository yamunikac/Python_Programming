"""
ITERATORS AND GENERATORS – COMPLETE BASIC DEMONSTRATION
"""


# -----------------------------
# 1️⃣ Iterator Example
# -----------------------------

numbers = [1, 2, 3, 4]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#Output
#1
#2
#3
#4


# -----------------------------
# 2️⃣ Custom Iterator Class
# -----------------------------

class CountDown:

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current


count = CountDown(3)

for num in count:
    print(num)

#Output
#3
#2
#1


# -----------------------------
# 3️⃣ Generator Example
# -----------------------------

def simple_generator():
    yield 1
    yield 2
    yield 3


for value in simple_generator():
    print(value)

#Output
#1
#2
#3


# -----------------------------
# 4️⃣ Generator with Loop
# -----------------------------

def square_generator(n):
    for i in range(n):
        yield i * i


for square in square_generator(5):
    print(square)

#Output
#0
#1
#4
#9
#16

