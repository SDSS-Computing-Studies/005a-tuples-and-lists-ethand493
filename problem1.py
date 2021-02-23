#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
myList = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
data1 = str(input("Enter a name that is on the list "))
data2 = str(input("Enter another word."))
number = int(myList.index(data1))
myList.remove(data1)
myList.insert(number, data2)
print(myList)
