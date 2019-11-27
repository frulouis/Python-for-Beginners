# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : strings.py
# @Software: PyCharm
# @Comments:  

# ======================================================================================
# Full Table Content
# Exercise 1.3.0: Working with Strings
# Exercise 1.3.1: String Concatenations (i.e. joining two or more strings)
# Exercise 1.3.2: String Formatting - Printing strings in a new Line
# Exercise 1.3.3: Printing strings with double quotes
# Exercise 1.3.4: Many string built in functions available in python
# Exercise 1.3.5: Stringing together fucntions
# Exercise 1.3.6: Checking Strings
# Exercise 1.3.7: String arrays and Slicing
# Exercise 1.3.8: String placeholders
# Exercise 1.3.9: Boolean Strings
# ======================================================================================


# **************************************************************************************
# Exercise 1.3.0: Working with Strings
# **************************************************************************************

# >>>
my_name = "Fru"
print("Hello, " + my_name + "!")

# **************************************************************************************
# Exercise 1.3.1: String Concatenations (i.e. joining two or more strings)
# **************************************************************************************

# >>>
my_name = "Fru"
my_age = "30"
print("Hello World! " + my_name + " is " + my_age + " years old!")

# **************************************************************************************
# Exercise 1.3.2: String Formatting - Printing strings in a new Line
# **************************************************************************************

# >>>
my_name = "Fru"
my_age = "30"
print("Hello World! This is " + my_name + ". \nHe is " + my_age + " years old.")

# **************************************************************************************
# Exercise 1.3.3: Printing strings with double quotes
# **************************************************************************************

# >>>
my_name = "Fru"
my_age = "30"
print("Hello World! This is " + my_name + ". \nHe is " + my_age + " \"years\" old.")

# **************************************************************************************
# Exercise 1.3.4: Many string built in functions available in python
# **************************************************************************************

# >>>
my_name = " Fru, Louis! "
my_age = "30"
print(my_age[0])  # counting starts with 0
print(len(my_name))
print(my_name.strip())  # returns "Fru, Louis!"
print(my_name.lower())
print(my_name.upper())
print(my_name.replace("F", "D"))
print(my_name.split(","))  # returns ['Fru', ' Louis!']

# **************************************************************************************
# Exercise 1.3.5: Stringing together fucntions
# **************************************************************************************

# >>>
my_name = "Fru"
my_age = "30"
print(my_name.isupper())  # False
print(my_name.upper().isupper())  # True

# **************************************************************************************
# Exercise 1.3.6: Checking Strings
# **************************************************************************************

# >>>
my_comment = "Threelly AI, is the best Chromeextension for YouTube - www.threelly.com"
test_phrase = "www" in txt  # Check if the phrase "www" is present in the following text:
print(test_phrase)

test_phrase = "wow" not in txt  # Check if the phrase "wow" is NOT present in the following text:
print(test_phrase)

# **************************************************************************************
# Exercise 1.3.7: String arrays and Slicing
# **************************************************************************************

# >>>
my_name = "Fru, Louis!"
print(my_name[1])  # Get the character at position 1 (remember that the first character has the position 0):

# >>>
my_name = "Fru, Louis!"
print(my_name[6:11])  # Get the characters from position 6 to position 11 (not included):

# >>> Negative indexing.
my_name = "Fru, Louis!"
print(b[-5:-2])  # Get the characters from position 5 to position 1, starting the count from the end of the string:

# **************************************************************************************
# Exercise 1.3.8: String placeholders
# **************************************************************************************

# >>>
my_first_name = "Fru"
my_last_name = "Louis"
my_age = "30"
my_introduction = "My name first name is {} , my last name is {} and I am {} years old."
print(my_introduction.format(my_first_name, my_last_name, my_first_name, my_age))

# >>>
my_first_name = "Fru"
my_last_name = "Louis"
my_age = "30"
my_introduction = "My name last name is {1} , my first name is {0} and I am {2} years old."
print(my_introduction.format(my_first_name, my_last_name, my_age))

# **************************************************************************************
# Exercise 1.3.9: Boolean Strings
# **************************************************************************************

# >>>
my_name = "Fru Louis"

print(my_name.isalnum())  # check if all char are numbers
print(my_name.isalpha())  # check if all char in the string are alphabetic
print(my_name.isdigit())  # test if string contains digits
print(my_name.istitle())  # test if string contains title words
print(my_name.isupper())  # test if string contains upper case
print(my_name.islower())  # test if string contains lower case
print(my_name.isspace())  # test if string contains spaces
print(my_name.endswith('s'))  # test if string endswith a s
print(my_name.startswith('H'))  # test if string startswith H
