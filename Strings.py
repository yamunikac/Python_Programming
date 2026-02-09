"""
Strings in Python:
- creating strings
- indexing
- slicing
- string methods
- checking methods
- replacing text
- splitting & joining
- formatting
- f-strings
"""

# -------------------------------
# CREATING STRINGS
# -------------------------------
name = "Yamunika"
course = 'Python'
message = """Learning Python is fun!"""
print(name)
print(course)
print(message)
#Output
#Yamunika
#Python
#Learning Python is fun!


# -------------------------------
# STRING INDEXING
# Accessing characters
# -------------------------------
text = "Python"
print(text[0])   # First character
print(text[-1])  # Last character
#Output
#P
#n


# -------------------------------
# STRING SLICING
# Extracting part of a string
# -------------------------------
word = "Developer"
print(word[0:4])
print(word[4:])
print(word[:5])
#Output
#Deve
#loper
#Devel


# -------------------------------
# STRING LENGTH
# -------------------------------
language = "Python"
print(len(language))
#Output
#6


# -------------------------------
# LOWER, UPPER, TITLE
# -------------------------------
text = "python programming"
print(text.upper())
print(text.lower())
print(text.title())
#Output
#PYTHON PROGRAMMING
#python programming
#Python Programming


# -------------------------------
# REMOVE SPACES
# -------------------------------
data = "   Yamunika   "
print(data.strip())
#Output
#Yamunika


# -------------------------------
# REPLACE TEXT
# -------------------------------
sentence = "I love Java"
updated = sentence.replace("Java", "Python")
print(updated)
#Output
#I love Python


# -------------------------------
# SPLIT STRING
# -------------------------------
skills = "Python,HTML,CSS"
print(skills.split(","))
#Output
#['Python', 'HTML', 'CSS']


# -------------------------------
# JOIN STRING
# -------------------------------
words = ["Full", "Stack", "Developer"]
result = " ".join(words)
print(result)
#Output
#Full Stack Developer


# -------------------------------
# CHECKING METHODS
# -------------------------------
text = "Python123"
print(text.isalpha())
print(text.isalnum())
print(text.isdigit())
#Output
#False
#True
#False


# -------------------------------
# STRING FORMATTING
# -------------------------------
name = "Yamunika"
age = 20
print("My name is {} and I am {} years old".format(name, age))
#Output
#My name is Yamunika and I am 20 years old


# -------------------------------
# F-STRINGS (Recommended)
# Modern and faster formatting
# -------------------------------
domain = "Full Stack Development"
print(f"{name} is learning {domain}")
#Output
#Yamunika is learning Full Stack Development


# -------------------------------
# COUNT & FIND
# -------------------------------
text = "python is powerful and python is easy"
print(text.count("python"))
print(text.find("powerful"))
#Output
#2
#10


# -------------------------------
# STRING REVERSAL
# -------------------------------
word = "Python"
reverse = word[::-1]
print(reverse)
#Output
#nohtyP
