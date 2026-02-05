#List...
fruits = ["apple", "banana", "mango", "apple"]
print(fruits)
print(fruits[1])
fruits.append("orange")
print(type(fruits))
fruits.insert(3,"Gua")
print(fruits)
fruits.extend(["cherry","grapes"])
print(fruits)
fruits.sort()
print(fruits)
fruits.pop(1)
print(fruits)
#Output
#['apple', 'banana', 'mango', 'apple']
#banana
#<class 'list'>
#['apple', 'banana', 'mango', 'apple', 'orange']
#['apple', 'banana', 'mango', 'Gua', 'apple', 'orange']
#['apple', 'banana', 'mango', 'Gua', 'apple', 'orange', 'cherry', 'grapes']
#['Gua', 'apple', 'apple', 'banana', 'cherry', 'grapes', 'mango', 'orange']
#['Gua', 'apple', 'banana', 'cherry', 'grapes', 'mango', 'orange']



#Tuple...
numbers = (10, 20, 30, 40, 20, 50)
print(numbers)
print(numbers[2])
print(type(numbers))
#Count Method (counts how many times a value appears)
print(numbers.count(20))
#Index Method (finds position of element)
print(numbers.index(40))
#Slicing (access multiple elements)
print(numbers[1:4])
#Length of tuple
print(len(numbers))
#Output
#(10, 20, 30, 40, 20, 50)
#30
#<class 'tuple'>
#2
#3
#(20, 30, 40)
#6



#Set...
values = {1, 2, 3, 3, 4}
print(values)
print(type(values))
#Add Method (adds one element)
values.add(5)
print(values)
#Update Method (adds multiple elements)
values.update([6, 7])
print(values)
#Remove Method (removes element, error if not found)
values.remove(2)
print(values)
#Discard Method (removes element, no error if not found)
values.discard(10)
print(values)
#Pop Method (removes a random element)
values.pop()
print(values)
#Union Method (combines two sets)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
#Intersection Method (common elements)
print(set1.intersection(set2))
#Difference Method (elements in set1 but not in set2)
print(set1.difference(set2))
#Clear Method (removes all elements)
set1.clear()
print(set1)
#Output (pop result may vary)
#{1, 2, 3, 4}
#<class 'set'>
#{1, 2, 3, 4, 5}
#{1, 2, 3, 4, 5, 6, 7}
#{1, 3, 4, 5, 6, 7}
#{1, 3, 4, 5, 6, 7}
#{3, 4, 5, 6, 7}   <-- random pop
#{1, 2, 3, 4, 5}
#{3}
#{1, 2}
#set()



#Dictionary...
student = {
    "name": "Yamunika",
    "age": 20,
    "course": "CSE"
}
print(student)
print(student["name"])
print(type(student))
#Add / Update value
student["age"] = 21
print(student)
#Using update() method
student.update({"college": "GIST"})
print(student)
#Get Method (safe way to access values)
print(student.get("course"))
#Keys Method
print(student.keys())
#Values Method
print(student.values())
#Items Method (key-value pairs)
print(student.items())
#Pop Method (removes specific key)
student.pop("age")
print(student)
#Popitem Method (removes last inserted pair)
student.popitem()
print(student)
#Clear Method (removes all elements)
student.clear()
print(student)
#Output
#{'name': 'Yamunika', 'age': 20, 'course': 'CSE'}
#Yamunika
#<class 'dict'>
#{'name': 'Yamunika', 'age': 21, 'course': 'CSE'}
#{'name': 'Yamunika', 'age': 21, 'course': 'CSE', 'college': 'GIST'}
#CSE
#dict_keys(['name', 'age', 'course', 'college'])
#dict_values(['Yamunika', 21, 'CSE', 'GIST'])
#dict_items([('name', 'Yamunika'), ('age', 21), ('course', 'CSE'), ('college', 'GIST')])
#{'name': 'Yamunika', 'course': 'CSE', 'college': 'GIST'}
#{'name': 'Yamunika', 'course': 'CSE'}
#{}

