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


# *********************************************LISTS***************************************
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