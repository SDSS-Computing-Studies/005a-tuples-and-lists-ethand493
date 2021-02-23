#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
table = []
a = str(input("Enter a word"))
table.append(a)
b = str(input("Enter a word"))
table.append(b)
c = str(input("Enter a word"))
table.append(c)
d = str(input("Enter a word"))
table.append(d)
e = str(input("Enter a word"))
table.append(e)

print(table)