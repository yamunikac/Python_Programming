#Basic List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = [num**2 for num in numbers]
print(squares)

#Output
#[1, 4, 9, 16, 25]


#List Comprehension with Condition
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

#Output
#[2, 4, 6]


#List Comprehension with if-else
numbers = [1, 2, 3, 4, 5]

labels = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(labels)

#Output
#['Odd', 'Even', 'Odd', 'Even', 'Odd']


#Nested List Comprehension
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

flattened = [num for row in matrix for num in row]
print(flattened)

#Output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]


#Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]

square_dict = {num: num**2 for num in numbers}
print(square_dict)

#Output
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#Set Comprehension
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = {num for num in numbers}
print(unique_numbers)

#Output
#{1, 2, 3, 4, 5}

