#Variable
a = 10
name = "Yamunika"
marks = 89.5
print(a)
print(name)
print(marks)
print(type(a))
#Output
#10
#Yamunika
#89.5
#<class 'int'>


#Dynamic Typing (Type can change)
x = 100
print(x)
print(type(x))
x = "Hello Python"
print(x)
print(type(x))
#Output
#100
#<class 'int'>
#Hello Python
#<class 'str'>


#Multiple Assignment
a, b, c = 10, 20, 30
print(a, b, c)
x = y = z = 5
print(x, y, z)
#Output
#10 20 30
#5 5 5


#Global Variable
num = 50
def show():
    print(num)
show()
#Output
#50


#Local Variable
def test():
    value = 25
    print(value)
test()
#Output
#25


#Delete Variable
temp = 10
print(temp)
del temp
#print(temp)  # This will cause an error
#Output
#10
