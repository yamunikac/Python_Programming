"""
OBJECT ORIENTED PROGRAMMING (OOP) – BASIC DEMONSTRATION
"""


# -----------------------------
# 1️⃣ Creating a Class
# -----------------------------

class Person:

    # Constructor (runs automatically when object is created)
    def __init__(self, name, age):
        self.name = name        # Instance Variable
        self.age = age

    # Method
    def greet(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# -----------------------------
# 2️⃣ Creating an Object
# -----------------------------

person1 = Person("Alice", 22)
person1.greet()

#Output
#My name is Alice and I am 22 years old.


# -----------------------------
# 3️⃣ Inheritance
# -----------------------------

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)   # Calling Parent Constructor
        self.grade = grade

    def display_grade(self):
        print(f"Grade: {self.grade}")


student1 = Student("Bob", 20, "A")
student1.greet()
student1.display_grade()

#Output
#My name is Bob and I am 20 years old.
#Grade: A


# -----------------------------
# 4️⃣ Polymorphism
# -----------------------------

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")


for animal in [Dog(), Cat()]:
    animal.speak()

#Output
#Bark
#Meow


# -----------------------------
# 5️⃣ Encapsulation (Basic)
# -----------------------------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance   # Private Variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
print("Balance:", account.get_balance())

#Output
#Balance: 1500

