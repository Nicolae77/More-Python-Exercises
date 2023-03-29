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





