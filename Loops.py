"""
Loops in Python:
- for loop
- while loop
- simulated do-while loop
- break, continue, pass
- nested loops
- loop with else
"""


# -------------------------------
# FOR LOOP
# -------------------------------
for i in range(1, 6):
    print(i)
#Output
#1
#2
#3
#4
#5


# -------------------------------
# WHILE LOOP
# -------------------------------
count = 1
while count <= 5:
    print(count)
    count += 1
#Output
#1
#2
#3
#4
#5


# -------------------------------
# DO-WHILE LOOP (Simulated)
# Python does not have a native do-while loop,
# but it can be created using while True.
# -------------------------------
num = 1
while True:
    print(num)
    num += 1
    if num > 5:
        break
#Output
#1
#2
#3
#4
#5


# -------------------------------
# BREAK STATEMENT
# Stops the loop immediately
# -------------------------------
for i in range(1, 10):
    if i == 5:
        break
    print(i)
#Output
#1
#2
#3
#4


# -------------------------------
# CONTINUE STATEMENT
# Skips the current iteration
# -------------------------------
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#Output
#1
#2
#4
#5


# -------------------------------
# PASS STATEMENT
# Acts as a placeholder
# -------------------------------
for i in range(1, 4):
    pass
print("Loop executed with pass")
#Output
#Loop executed with pass


# -------------------------------
# NESTED LOOPS
# Loop inside another loop
# -------------------------------
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
#Output
#1 1
#1 2
#2 1
#2 2
#3 1
#3 2


# -------------------------------
# LOOP WITH ELSE
# Executes when loop finishes normally
# -------------------------------
for i in range(1, 4):
    print(i)
else:
    print("Loop completed")
#Output
#1
#2
#3
#Loop completed


# -------------------------------
# ITERATING THROUGH A LIST
# -------------------------------
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)
#Output
#Apple
#Banana
#Mango


# -------------------------------
# SUM OF NUMBERS USING LOOP
# -------------------------------
total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)
#Output
#Sum: 15

