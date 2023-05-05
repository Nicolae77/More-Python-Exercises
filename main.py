# **************************************** STRING EXERCISES ********************************************* 

# Exercise nr.1
# Using negative index get the last character from the string.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string[-1])


# Exercise nr.2
# Using positive index return exclamation mark from the string.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string[5])


# Exercise nr.3
# Using negative index return the b character from the string.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string[-12])


# Exercise nr.4
# Insert a method in order to return the index of the I character from the string.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.index("I"))


# Exercise nr.5
# Insert the correct method in order to return the number of occurrences of the letter e in the string.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.count("e"))


# Exercise nr.6
# Insert a method to convert all letters from the string to uppercase
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.upper())


# Exercise nr.7
# Insert a method in order to get the index at which the substing 'My' starts.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.find("My"))


# Exercise nr.8
# Insert the correct method in order to check if the strings starts with the letter N. 
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.startswith("N")) # return False
print(text_string.startswith("H")) # return True


# Exercise nr.9
# Insert the correct method in order to convert all uppercase letters to lowercase and all lowercase letters to uppercase.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.swapcase())


# Exercise nr.10
# Insert the correct method in order to remove all spaces.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.replace(" ",""))


# Exercise nr.11
# insert the correct method in order to replace all the occurences of letter e with substring abc.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.replace('e', 'abc'))


# Exercise nr.12
# Insert the correct method in order to split entire string in two parts, using comma as a delimiter.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.split(","))


# Exercise nr.13
# Insert the correct method in order to join the characters of the string using the & symbol as a delimiter.
text_string = "Hello! My name is Nick, I am web developer."
print("&".join(text_string))


# Exercise nr.14
# Insert the correct code in order to concatenate text_string with next_string.
text_string = "Hello! My name is Nick, I am web developer."
next_string = " I am specialized in Python, Django, and Flask"
print(text_string + next_string)


# Exercise nr.15
# Insert the correct method in order to convert the first letter of each word in the string to uppercase.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.title())


# Exercise nr.16
# Using string formating with the % operator map the value of: Hello, Nick, and I corresponding formatting operators.
text_string = "%s! My name is %s, %s am web developer."
print(text_string % ("Hello", "Nick", "I"))


# Exercise nr.17
# Using string formating with the format() method map the value of Hello, Nick, and I to the corresponding formatting operators.
text_string = "{}! My name is {}, {} am web developer."
print(text_string.format("Hello", "Nick", "I"))


# Exercise nr.18
# Using slicing in order to return substring Nick from the string. Use positive indexes.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string.index("N"))
print(text_string.index("k"))
print(text_string[18:22])


# Exercise nr.19
# Using slicing in order to return substring Nick from the string. Use negative indexes.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string[-25:-21])


# Exercise nr.20
# Using slising return the first 10 characters in the string. Use a single positive index.
text_string = "Hello! My name is Nick, I am web developer."
new_string = text_string[:10]
print(len(new_string))
print(new_string)



# Exercise nr.21
#  Using slicing return the last 12  characters in the string. Use a single negative index.
text_string = "Hello! My name is Nick, I am web developer."
new_str = text_string[-12:]
print(len(new_str))
print(new_str)


# Exercise nr.22
# Using slicingreturn the entire string in reversed order.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string[::-1])


# Exercise nr.23
# Using slicing return every 5th character of the string, starting with the first character.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string[::5])


# Exercise nr.24
# Using slicing return the string except the first 5 characters. Use a single, positive index.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string[5:])


# Exercise nr.25
# Using the slicing return the string except the last 9 characters. Use a single, negative index.
text_string = "Hello! My name is Nick, I am web developer."
print(text_string[:-7])


# *********************************************NUMBERS and BOOLEANS***************************************
# Exercise nr.26
# Use the correct function in order to convert number1 from integer to float.
number1 = 15
number2 = float(number1)
print(type(number2))


# Exercise nr.27
# Use the correct function to convert number1 from float to integer.
number1 = 15.25
number2 = int(number1)
print(type(number2))


# Exercise nr.28
# Use the correct math operator in number3 to get reminder between number1 and number2.
number1 = 27
number2 = 8
number3 = number1 % number2
print(number3)


# Exercise nr.29
# Use the correct math operator between number1 and number2 in order to obtain number1 square.
number1 = 10
number2 = 2
number3 = number1 ** number2
print(number3)


# Exercise nr.30
# Use number1 and number2 in order to return True, between value of number3 and modulo.
number1 = 11
number2 = 2
number3 = number1 // number2
print(number3)
modulo = 29 % 8
print(modulo)
print(number3 == modulo)


# Exercise nr.31
# Use absolute function to return absolute value of the number1.
# Ex: The absolute value of -5 is 5.
number1 = -12
number2 = abs(number1)
print(number2)


# Exercise nr.32
# Use the correct function to raise number1 to the power of number2.
number1 = 10
number2 = 2
number3 = pow(number1, number2)
print(number3)


# Exercise nr.33
# Use logical operator between two expressions to return the final result False
result = ((24 / 8) % 3 == 0) and ((abs(-18) / 6 - 1) > 3)
print(result)



# Exercise nr.34
# Use logical operator between two expressions to return the final result True
result = (min(pow(2, abs(2)), 9) == 4 ** 2 - 12) or (44 % 20 + 10 > 4 ** 2)
print(result)


# Exercise nr.35
# Use the correct function in order to get final result False.
result = bool(150 % (10 ** 2 / 4))
print(result) 


# LISTS  (A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements).
# Exercise nr.36
# Use the correct method to find out the number of elements in the list.
lst = [1, 2.4, 'Python', 20, 'Nick']
result = len(lst)
print(result)


# Exercise nr.37
# Use the correct method in order to remove the element from the list located at index 3.
lst = [1, 2.4, 'Python', 20, 'Nick']
lst.pop(3)
print(lst)


# Exercise nr.38
# Use the correct method in order to add the element 'Developer' at the end of the list.
lst = [1, 2.4, 'Python', 20, 'Nick']
lst.append('Developer')
print(lst)


# Exercise nr.39
# Use the correct method in order to remove the element 'Python' from the list.
lst = [1, 2.4, 'Python', 20, 'Nick']
lst.remove('Python')
print(lst)


# Exercise nr.40
# Use the correct method in order to return the index of the element 2.4 from the list.
lst = [1, 2.4, 'Python', 20, 'Nick']
indx = lst.index(2.4)
print(indx)


# Exercise nr.41
# Use the correct method in order to insert the element 'Django' at index 3 in the list.
lst = [1, 2.4, 'Python', 20, 'Nick']
lst.insert(3, 'Django')
print(lst)


# Exercise nr.42
# Use the corect method in order to concatenate lst1 with lst2.
lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
lst1.extend(lst2)
print(lst1)


# Exercise nr.43
# Use the correct method in order to find out how many times does element 3 occur in the list.
lst = [1, 3, 2, 3, 4, 5, 6, 3, 7, 3]
result = lst.count(3)
print(result)


# Exercise nr.44
# Use the correct method in order to sort the elements of the list in ascending order.
lst = [2, 4, 2, 1, 6, 8, 9, 0]
result = sorted(lst)
print(result)


# Exercise nr.45
# Use the correct function in order to sort the elements from the list in descending order.
lst = [7, 3, 5, 8, 9, 1, 6, 2, 4]
result = sorted(lst, reverse=True)
print(result)


# Exercise nr.46
# Use the correct function in order to find out the smallest number from the list.
lst = [7, 3, 5, 8, 9, 1, 6, 2, 4]
result = min(lst)
print(result)


# Exercise nr.47
# Use the correct function in order to find out the largest number from the list.
lst = [7, 3, 5, 8, 9, 1, 6, 2, 4]
result = max(lst)
print(result)

# Exercise nr.48
# Use the correct function in order to get the sum of all elements fromthe list.
lst = [7, 3, 5, 8, 9, 1, 6, 2, 4]
result = sum(lst)
print(result)

# Exercise nr.49
# Use the correct function in oredr to delete all elements from the list.
lst = [7, 3, 5, 8, 9, 1, 6, 2, 4]
lst.clear()
print(lst)


# Exercise nr.50
# Use the correct operators and parantheses in order to add the element [4, 5, 6] to the list and multiply the resulting list by 2.
lst = [1, 2, 3]
add = (lst + [4, 5, 6]) * 2
print(add)


# Exercise nr.51
# Use the correct code in order to return the element 'Python' from the list.
lst = [1, 2.3, 'Django', 'Python']
result = lst[3]
print(result)


# Exercise nr.52
# Use the correct code in order to return the element 'Django' from the list based on its negative index.
lst = [1, 2.3, 'Django', 'Python']
result = lst[-2]
print(result)


# Exercise nr.53
# Use the correct code in order to return a slice of ['Django', 'Python'] based on positive indexes.
lst = [1, 2.3, 'Django', 'Python', 'Developer']
result = lst[2:4]
print(result)


# Exercise nr.54
# Use the correct code in order to return a slice of ['Django', 'Python'] based on negative indexes.
lst = [1, 2.3, 'Django', 'Python', 'Developer']
result = lst[-3:-1]
print(result)

# Exercise nr.55
# Use the correct code in order to return list except the first 3 elements, using a single, positive index.
lst = [1, 2.3, 'Django', 'Python', 'Developer']
result = lst[3:]
print(result)


# Exercise nr.56
# Use the correct code in order to return list except the last 4 elements, using a single, negative index.
lst = [1, 2.3, 'Django', 'Python', 'Developer']
result = lst[:-4]
print(result)


# Exercise nr.57
# Use the correct code in oredr to return the list except the first 3 elements, using negative index.
lst = [1, 2.3, 'Django', 'Python', 'Developer', 'Nick', True]
result = lst[-4:]
print(result)


# Exercise nr.58
# Use the correct code in oredr to return the list except the last 2 elements, using a single, positive index.
lst = [1, 2.3, 'Django', 'Python', 'Developer', 'Nick', True]
result = lst[:5]
print(result)


# Exercise nr.59
# Use the correct code in oredr to return every second element of the list, starting with the first element of the list.
lst = [1, 2.3, 'Django', 'Python', 'Developer', 'Nick', True]
result = lst[::2]
print(result)


# Exercise nr.60
# Use the correct code in oredr to return every third element of the list starting with the last element of the list.
lst = [1, 2.3, 'Django', 'Python', 'Developer', 'Nick', True]
result = lst[::-3]
print(result)


# Exercise nr.61
# Use the correct function in order to convert the list to a set.
lst = [1, 2, 3, 4, 5, 6, 7, 8]
new_set = set(lst)
print(new_set)


# Exercise nr.62
# Use the correct function in order to convert the list to a frozen set.
lst = [1, 2, 3, 4, 5, 6, 7, 8]
frz_set = frozenset(lst)
print(type(frz_set))


# SET (A set is a collection which is unordered, unchangeable*, and unindexed.)
# A set is a collection of unique data. That is, elements of a set cannot be duplicate.
# Exercise nr.63
# Use the correct code to verify if element 9 is in set1.
set1 = {1, 2, 3, 4, 5, 6}
check = 9 in set1
print(check)


# Exercise nr.64
# Use the correct code in order to add the element 9 to set1.
set1 = {1, 2, 3, 4, 5, 6}
set1.add(9)
print(set1)


# Exercise nr.65
# Use the correct code in order to remove the element 5 from set1.
set1 = {1, 2, 3, 4, 5, 6}
set1.remove(5)
print(set1)


# Exercise nr.66
# Use the correct code in order to find out the common elements of set1 and set2.
set1 = {1, 3, 5, 6, 0, 2}
set2 = {3, 5, 9, 10, 12}
common = set1.intersection(set2)
print(sorted(list(common)))


# Exercise nr.67
# Use the correct code in order to join the elements of set1 and set2.
set1 = {1, 3, 5, 6, 0, 2}
set2 = {3, 5, 9, 10, 12}
join = set1.union(set2)
print(sorted(list(join)))


# Exercise nr.68
# Use the correct code in order to find out the elements of set2 that are not members of set1.
set1 = {1, 3, 5, 6, 0, 2}
set2 = {3, 5, 9, 10, 12}
result = set2.difference(set1)
print(sorted(list(result)))


# Tuples (A tuple is a collection which is ordered and unchangeable).
#  Exercise nr.69
# Use the correct method in orde to find out the number of elements in tup.
tup = ('Moldova', 'Romania', 'Estonia', 'Bulgaria', 'France', 'Spain')
result = len(tup)
print(result)


#  Exercise nr.70
# Use the correct method in order to find out the index of 'Bulgaria'.
tup = ('Moldova', 'Romania', 'Estonia', 'Bulgaria', 'France', 'Spain')
indx = tup.index('Bulgaria')
print(indx)


#  Exercise nr.71
tup = ("Moldova", "Romania", "Spain")
(mo, ro, sp) = tup 
print(mo + ", " + ro + ", " + sp)


#  Exercise nr.72
# Use the correct method in order to find out the last element of tup in alphabetical order.
tup = ("Moldova", "Romania", "Spain", "Estonia")
last = max(tup)
print(last)


#  Exercise nr.73
# Use the correct method in order to find out the number of occurrences of Spain in tup.
tup = ("Moldova", "Romania", "Spain", "Estonia", "France", "Spain")
result = tup.count("Spain")
print(result)


#  Exercise nr.74
# Use the correct slice in order to return all elements of tup, except the first two, using a negative index.
tup = ("Moldova", "Romania", "Spain", "Estonia", "France", "Spain")
result = tup[-4:]
print(result)


#  Exercise nr.75
# Use the correct slice in order to return all elements of tup, except the last two, using a negative index.
tup = ("Moldova", "Romania", "Spain", "Estonia", "France", "Spain")
result = tup[:-2]
print(result)


#  Exercise nr.76
# Use the correct slice in order to return all elements of tup, except the first two, using a positive index.
tup = ("Moldova", "Romania", "Spain", "Estonia", "France", "Spain")
result = tup[2:]
print(result)


#  Exercise nr.77
# Use the correct slice in order to return all elements of tup, except the last two, using a positive index.
tup = ("Moldova", "Romania", "Spain", "Estonia", "France", "Spain")
result = tup[:4]
print(result)


# Ranges
#  Exercise nr.78
# Use the correct function to return a list of range of consecutive integers from 0 to 9.
rng = range(10)
print(list(rng))


#  Exercise nr.79
# Use the correct function in order to return a list of range of consecutive integers from 0 to 9 inclusively, use two arguments.
rng = range(0, 10)
print(list(rng))


#  Exercise nr.80
# Use the correct function in order to return a range of consecutive integers from 20 to 30.
rng = range(20, 31)
print(list(rng))


#  Exercise nr.81
#  Use the correct range function in order to return [1, 3, 5, 7, 9].
rng = range(1, 10, 2)
print(list(rng))


#  Exercise nr.82
# Use the correct range function in order to return [115, 120]
rng = range(115, 125, 5)
print(list(rng))


#  Exercise nr.83
# Use the correct range function in order to return [-40, -30, -20]
rng = range(-40, -10, 10)
print(list(rng))


#  Exercise nr.84
# Use the correct range function in order to return [-40, -20, 0, 20, 40]
rng = range(-40, 50, 20)
print(list(rng))


#  Exercise nr.85
# Use the correct range function in order to return [-20]
rng = range(-20, -19)
print(list(rng))


# *****************   Dictionaries   *************************
#  Exercise nr.86
# Use the correct code to return the value associated with key 3.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
result = user_details[3]
print(result)


#  Exercise nr.87
# Use the correct code to return the value associated with key 3. Use get method.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
result = user_details.get(3)
print(result)


#  Exercise nr.88
# Use the correct code in order to update the value associated with key 3 to email.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
user_details[3] = "email"
print(user_details[3])


#  Exercise nr.89
# Use the correct code to add a new key-value pair to the dictionary: 4: "coutry"
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
user_details[4] = "country"
print(user_details)


#  Exercise nr.90
# Use the correct code to return the number of key-value pairs in the dictionary.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
result = len(user_details)
print(result)


#  Exercise nr.91
# Use the correct code in order to delete the key-value pair associated with key 2
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
del user_details[2]
print(user_details)


#  Exercise nr.92
# Use the correct code in order to delete the key-value pair associated with key 3, use pop method.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
user_details.pop(3)
print(user_details)


#  Exercise nr.93
# Use the correct code in order to verify that 5 is not a key in the dictionary.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
check = 5 not in user_details
print(check)


#  Exercise nr.94
# Use the correct method in order to delete all the elementsd from dictionary.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
user_details.clear()
print(user_details)


#  Exercise nr.95
# Use the correct method in order to get a list of tuple, where each tuple represents a key-value pair in the dictionary.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
result = user_details.items()
print(result)

#  Exercise nr.96
# Use the correct function in order to get the sum of all keys in the dictionary.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
result = sum(user_details)
print(result)


#  Exercise nr.97
# Use the correct method in order to get a list of all values in the dictionary.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
result = user_details.values()
print(result)


#  Exercise nr.98
# Use the correct function in order to get the smallest key in the dictionary.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
small_key = min(user_details)
print(small_key)


#  Exercise nr.99
# Use the correct method in order to get a list of all keys in the dictionary.
user_details = {1: 'first name', 2: 'last name', 3: 'address'}
key = user_details.keys()
print(key)


#  Exercise nr.100
# Use the correct method in order to return and remove an arbitrary key-value pair from the dictionary.
user_details = {1: 'first name', 2: 'last name', 3: 'address', 4: 'email'}
user_details.popitem()
print(user_details)


# *****************    Data Type Conversions    ************************************
#  Exercise nr.101
# Use the correct function in order to convert integer to a string.
integer = 20
convert = str(integer)
print(type(convert))
print(convert)


#  Exercise nr.102
# Use the correct function in order to convert string to a integer.
string = '25'
convert = int(string)
print(type(convert))
print(convert)


#  Exercise nr.103
# Use the correct function in order to convert string in floating-point number.
integer = 59
convert = float(integer)
print(type(convert))
print(convert)


#  Exercise nr.104
# Use the correct function in order to convert string to a list.
string = 'Developer'
convert = list(string)
print(type(convert))
print(convert)


#  Exercise nr.105
# Use the correct function in order to convert list to a tuple.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
convert = tuple(lst)
print(type(convert))
print(convert)


#  Exercise nr.106
# Use the correct function in order to convert tuple to frozenset.
tpl = (1, 2, 3, 4, 5, 6, 7)
convert = frozenset(tpl)
print(type(convert))
print(convert)


#  Exercise nr.107
# Use the correct function in order to convert integer to a binary
integer = 10
convert = bin(integer)
print(convert)


#  Exercise nr.108
# Use the correct function in order to convert integer to a hexadecimal
integer = 10
convert = hex(integer)
print(convert)


#  Exercise nr.109
# Use the correct function in order to convert binary to decimal.
binary = '0b1010'
convert = int(binary, 2)
print(convert)


#  Exercise nr.110
# Use the correct function in order to convert hexadecimal to decimal notation.
hexadecimal = '0xa'
convert = int(hexadecimal, 16)
print(convert)


# *********************************  CONDITIONALS  *********************
#  Exercise nr.111
# Write a code that peints out True if y has 20 characters or more.
y = 'Python is the most popular programming language.'
print(len(y))
if len(y) >= 20:
    print("y, has 20 or more characters")


#  Exercise nr.112
# Write a code that prints out True, if y is string and the first character inthe string is P.
y = 'Python is the most popular programming language.'
if type(y) is str and y.startswith("P"):
    print("True")

#  Exercise nr.113
# Write a code that prints out True, if at least one of the following conditions occurs:
# 1. the string contains the character 'w'.
# 2. the string contains the character 'o' 4 times.
y = 'Python is the most popular programming language.'
print(y.count('o'))
if 'w' in y or y.count('o') >= 4:
    print('True')


#  Exercise nr.114
# Write a code that prints out True, if index of letter 'o' is less than 5 and prints out False if the same condition is not satisfied.
y = 'Python is the most popular programming language.'
print(y.index('o'))
if y.index('o') < 5:
    print("True")
else:
    print("False")


#  Exercise nr.115
# Write a code that prints out True if the last 4 characters of the string are digits and prints out False otherwise.
y = 'Python is the most popular programming language in 2023'
if y[-4:].isdigit():
    print("True")
else:
    print("False")


#  Exercise nr.116
# Write a code that prints out True, if y has at least 4 elements and the element positionedat index 3 is a boolean and prints out Falseotherwise.

print(len(y))
if len(y) >= 4 and type(y[3]) is bool:
    print("True")
else:
    print("False")


#  Exercise nr.117
# Write a code that prints out True if the second string of the first list in y ends with the letter 'h' and the first string of the second list in y also ends with the letter 'h', and prints out False otherwise.
y = ['Python', 'Django', 4, True, 23.45, ["length", "width", "height"], 7, 10, ["length", "width", "height"]]
if y[5][1].endswith("h") and y[8][0].endswith("h"):
    print("True")
else:
    print("False")


#  Exercise nr.118
# Write a code that prints out True if one of the following two conditions are satisfied and prints out False otherwise.
# 1. The third string of the first list in y ends with the letter 'h'.
# 2. The second string of the second list in y also ends with the letter 'h'.
y = ['Python', 'Django', 4, True, 23.45, ["length", "width", "height"], 7, 10, ["length", "width", "height"]]
if y[5][2].endswith("h") or y[8][1].endswith("h"):
    print("True")
else:
    print("False")


#  Exercise nr.119
# Write a code that prints out True if the largest value among the first 3 elements of the list is less than or equal to the smallest value among the next 3 elements of the list. Otherwise, print out False.
x = [115, 116, 117, 109, 115, 120, ["length", "width", "height"]]
print(x[:3])
print(x[3:6])
if max(x[:3]) <= min(x[3:6]):
    print("True!")
else:
    print("False!")



#  Exercise nr.120
# Write a code that prints out True if 110 appears at least once inside the list or if it is the second element in the list
x = [110, 116, 117, 109, 110, 120, ["length", "width", "height"]]
if x.count(110) >= 1 or x.index(110) == 1:
    print("True")
else:
    print("False")


#  Exercise nr.121
# Write a code that prints out True if the value associated with kye number 3 is Django or the number of kye-value pairs in the dictionary divided by 4 returns a reminder less than 2.
y = {1: 'Python', 2: 'Developer', 3: 'Django'}
if y[3] == 'Django' or len(y) % 4 < 2:
    print("True!")
else:
    print('False!')

print(len(y) % 4)



#  Exercise nr.122
# Write a code that prints out True if 3 is a key value in the dictionary and the smallest value(alphabetical) in the dictionary is C#, Otherwise print False.
y = {1: 'Python', 2: 'Developer', 3: 'Django', 4: 'C#'}
if 3 in y and sorted(y.values())[0] == "C#":
    print("True")
else:
    print("False")


#  Exercise nr.123
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
 
if sorted(x.values())[-1][-1] == "n":
    print("True!")
else:
    print("False!")
print(sorted(x.values()))
print(sorted(x.values())[-1])
print(sorted(x.values())[-1][-1])


#  Exercise nr.124
# Write code that prints out True! if the largest key in the dictionary divided by the second largest key in the dictionary returns a remainder equal to the smallest key in the dictionary. Otherwise, print out False!
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if sorted(x.keys())[-1] % sorted(x.keys())[-2] == sorted(x.keys())[0]:
    print("True!")
else:
    print("False!")


#  Exercise nr.125
# Write code that prints out True! if the sum of all the keys in the dictionary is less than the number of characters of the string obtained by concatenating the values associated with the first 5 keys in the dictionary. Otherwise, print out False!
x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
print(sum(x))
print(len(x[1] + x[2] + x[3] + x[4] + x[5]))
if sum(x) < len(x[1] + x[2] + x[3] + x[4] + x[5]):
    print("True!")
else:
    print("False!")

#  Exercise nr.126
# Write code that prints out True! if the 3rd element of the first range is less than 2, prints out False! if the 5th element of the first range is 5, and prints out None! otherwise.
y = [list(range(6)), list(range(5,10)), list(range(1,11,3))]
print(y[0])
print(y[1])
print(y[2])
if y[0][2] < 2:
    print("True")
elif y[0][4] == 5:
    print("False")
else:
    print("None")


#  Exercise nr.127
# Write code that prints out True! if the 3rd element of the 3rd range is less than 6, prints out False! if the 1st element of the second range is 5, and prints out None! otherwise.
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
print(x[2][2])
print(x[1][0])
if x[2][2] < 6:
    print("True!")
elif x[1][0] == 5:
    print("False!")
else:
    print("None!")


#  Exercise nr.128
# Write code that prints out True! if the last element of the first range is greater than 3, prints out False! if the last element of the second range is less than 9, and prints out None! otherwise.

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
print(x[0][-1])
print(x[1][-1])
if x[0][-1] > 3:
    print("True!")
elif x[1][-1] < 9:
    print("False!")
else:
    print("None")


#  Exercise nr.129
# Write code that prints out True! if the length of the first range is greater than or equal to 5, prints out False! if the length of the second range is 4, and prints out None! otherwise.
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
print(len(x[0]))
print(len(x[1]))
if len(x[0]) >= 5:
    print("True!")
elif len(x[1]) == 4:
    print("False!")
else:
    print("None!")


#  Exercise nr.130
# Write code that prints out True! if the sum of all the elements of the first range is greater than the sum of all the elements of the third range, prints out False! if the largest element of the second range is greater than the largest element of the third range, and prints out None! otherwise.

x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]
print(sum(x[0]), sum(x[2]))
print(max(x[1]), max(x[2]))
if sum(x[0]) > sum(x[2]):
    print("True!")
elif max(x[1]) > max(x[2]):
    print("False!")
else:
    print("None!")


#  Exercise nr.131
# Write code that prints out True! if the largest element of the first range minus the second element of the 3rd range is equal to the first element of the first range, prints out False! if the length of the first range minus the length of the 2nd range is equal to the first element of the 3rd range, prints out Maybe! if the sum of all the elements of the 3rd range divided by 2 returns a remainder of 0, and prints out None! otherwise.
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

if max(x[0]) - x[2][1] == x[0][0]:
    print("True!")
elif len(x[0]) - len(x[1]) == x[2][0]:
    print("False!")
elif sum(x[2]) % 2 == 0:
    print("Maybe!")
else:
    print("None!")


#  Exercise nr.132
# Write code that prints out True! if the sum of the last 3 elements of the first range plus the sum of the last 3 elements of the 3rd range is equal to the sum of the last 3 elements of the 2nd range, and prints out False! if the length of the first range times 2 is less than the sum of all the elements of the 3rd range.
x = [list(range(5)), list(range(5,9)), list(range(1,10,3))]

if sum(x[0][-3:]) + sum(x[2][-3:]) == sum(x[1][-3:]):
    print("True!")
elif len(x[0] *2) <= sum(x[2]):
    print("False!")


#  Exercise nr.133
# Write code that prints out True! if the 2nd character of the value at key 1 is also present in the value at key 4, and prints out False! otherwise.

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
print(x[1][1])
print(x[4])
if x[1][1] in x[4]:
    print("True!")
else:
    print("False!")


#  Exercise nr.134
# Write code that prints out True! if the second to last character of the value at key 3 is the first character of the value at key 5, and prints out False! otherwise.

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}

if x[3][-2] == x[5][0]:
    print("True!")
else:
    print("False!")



#  Exercise nr.135
# Write code that prints out True! if the number of characters of the smallest value in the dictionary is equal to the number of occurrences of letter a in the value at key 3, and prints out False! otherwise.

x = {1: "Python", 2: "Java", 3: "Javascript", 4: "Ruby", 5: "Perl", 6: "C#", 7: "C++"}
print(len(min(x.values())))
print(x[3].count("a"))
if len(min(x.values())) == x[3].count("a"):
    print("True!")
else:
    print("False!")


# ********************************* LOOPS ******************************
#  Exercise nr.136
# Write a loop that iterates over the y list and prints out all the elements of the list.
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in y:
    print(i)


#  Exercise nr.137
# Write a loop that iterates over the y list and prints out the remainders of each element of the list divided by 3.
print('Elements of the list divided by 3')
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in y:
    if i % 3 == 0:
        print(i)


#  Exercise nr.138
# Write a for loop that iterates over the y list and prints out all the elements of the list in reversed order and multiplied by 2.
print('sorted list')
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in sorted(y, reverse=True):
    print(i * 2)

#  Exercise nr.139
# Write a for loop that iterates over the y list and prints out all the elements of the list divided by 2 and the string 'Well Done'! after the list is exhausted.
print('Division by 2')
y = [4, 8, 12, 16, 20, 24, 28, 32, 36]
for i in y:
    print(int(i / 2))
else:
    print('Well Done')


#  Exercise nr.140
# Write a for loop that iterates over the y list and prints out the index of each element.
print('Index of each element')
y = [4, 8, 12, 16, 20, 24, 28, 32, 36]
for i in y:
    print(y.index(i))
    

#  Exercise nr.141
# Write a while loop that prints out the value of y squared while y is less than or equal to 10.
print('y squared while y is less than or equal to 10')
y = 0
while y <= 10:
    print(y ** 2)
    y += 1


#  Exercise nr.142
# Write a while loop that prints out the value of y times 10 while y is less than or equal to 5 and then prints out 'Well Done'! when y becomes larger than 5.
y = 0
while y <= 5:
    print(y * 10)
    y += 1
else:
    print('Well Done')


#  Exercise nr.143
# Write a while loop that prints out the value of y plus 10 while y is less than or equal to 15 and the remainder of y divided by 5 is 0.
y = 10
while y <= 15 and y % 5 == 0:
    print(y + 10)
    y += 1


#  Exercise nr.144
# Write a while loop that prints out the absolute value of y while y is negative.
y = -5
while y < 0:
    print(abs(y))
    y += 1


#  Exercise nr.145
# Write a while loop that prints out the value of x times y while x is greater than or equal to 5 and less than 10, and prints out the result of x divided by y when x becomes 10.
print('while for x and y')
x = 5
y = 2
while x >= 5 and x < 10:
    print(x * y)
    x += 1
else:
    print(x / y)


#  Exercise nr.146
# Write code that will iterate over the y list and multiply by 2 only the elements that are greater than 10 and print them out to the screen.
y = [1, 4, 6, 7, 10, 11, 22, 33]
for i in y:
    if i > 10:
        print(i * 2)


#  Exercise nr.147
# Write code that will iterate over the x and y lists and multiply each element of x with each element of y, also printing the results to the screen.
x = [1, 2, 3, 4]
y = [2, 3]
for i in x:
    for j in y: 
        print(i * j)


#  Exercise nr.148
# Write code that will iterate over the x and y lists and multiply each element of x with each element of y that is less than 12, also printing the results to the screen.
x = [2, 4, 6, 8]
y = [5, 10, 15, 20]
print('')
for i in x:
    for j in y:
        if j < 12:
            print(i * j)


#  Exercise nr.149
# Write code that will iterate over the x and y lists and multiply each element of x that is greater than 5 with each element of y that is less than 12, also printing the results to the screen.
x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for i in x:
    for j in y:
        if i > 5 and j < 12:
            print(i * j)
            
