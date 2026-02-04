#Simple if
age = 18
if age >= 18:
    print("Eligible to vote")
#Output
#Eligible to vote


#if-else
num = 7
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
#Output
#Odd Number


#if-elif-else
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
#Output
#Grade B


#Nested if
number = 10
if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
#Output
#Positive Even Number


#Short Hand if (Ternary Operator)
a = 20
b = 15
print("A is greater") if a > b else print("B is greater")
#Output
#A is greater

