# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : introduction.py
# @Software: PyCharm
# @Comments:  

# ======================================================================================
# Full Table Content
# Exercise 0.0.0: Hello World!
# Exercise 0.0.1: This is a comment. This code cannot run.
# Exercise 0.0.2: Print Numbers and Variables.
# Exercise 0.0.3: Print Strings and set Variables.
# Exercise 0.0.4: More variables, strings and concatenation.
# Exercise 0.0.5: Booleans & Conditionals.
# Exercise 0.0.6: Conditionals and boolean logic.
# Exercise 0.0.7: Python Indentation.
# Exercise 0.0.8: Save this file and run it from the Command line, instead of pycharm.
# ======================================================================================


# Write a program to print the word "Hello World" to the screen.


# **************************************************************************************
# Exercise 0.0.0: Hello World!
# **************************************************************************************
print("Hello World")

# **************************************************************************************
# Exercise 0.0.1: This is a comment. This code cannot run.
# **************************************************************************************

# >>>
# This is a comment
print("Hello, World!")

# >>>
print("Hello, World!")  # This is a comment

# >>>
# This is a comment
# written in
# more than just one line
print("Hello, World!")

# >>>
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# **************************************************************************************
# Exercise 0.0.2: Print Numbers and Variables
# **************************************************************************************

# >>>
a = 1
print(a)
print(a + 1)

# **************************************************************************************
# Exercise 0.0.3: Print Strings and set Variables
# **************************************************************************************

# >>>
character_name = "Fru"
print("Hello, " + character_name + "!")

# >>>
character_name = "Fru"
# is the same as
character_name = 'Fru'

# >>>: Python allows you to assign values to multiple variables in one line:
first, middle, last = "Fru", "Louis", "Nde"
print(first)
print(middle)
print(last)

# >>>: Python allows you to assign values to multiple variables in one line:
first = middle = last = "Fru"
print(first)
print(middle)
print(last)

# **************************************************************************************
# Exercise 0.0.4: More variables, strings and concatenation.
# **************************************************************************************

# >>> Combining two Strings.
character_name = "Fru"
character_age = "30"
print("Hello World! " + character_name + " is " + character_age + " years old.")

# >>> This won't work. Can't concat a String to a Double. The datatypes are different.
character_name = "Fru"
character_age = 30
print(character_name + character_age)

# **************************************************************************************
# Exercise 0.0.5: Booleans & Conditionals
# Note: The bool() function allows you to evaluate any value, and give you True or False in return
# **************************************************************************************

# >>>
print(5 > 8)
print(5 == 6)
print(5 < 7)
print(bool("Fru"))
print(bool(3))

# **************************************************************************************
# Exercise 0.0.6: Conditionals and boolean logic.
# **************************************************************************************

# >>>
my_age = 30
your_age = 57

if my_age > your_age:
    print("I am older than you")
else:
    print("You are older than me")

# **************************************************************************************
# Exercise 0.0.7: Python Indentation.
# **************************************************************************************

# >>>
# Key Point - You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

# This works.
if 5 > 2:
    print("Five is greater than two!")

# >>>
# Syntax Error. Indentation not correct.
if 5 > 2:
    print("Five is greater than two!")

# >>>
# This works: Key point -The number of spaces is up to you as a programmer, but it has to be at least one.
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")

# >>>
# This works: Again, You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")

# **************************************************************************************
# Exercise 0.0.8: Save this file and run it from the Command line, instead of pycharm.
# e.g. C:\Users\Your Name>python myfile.py
# **************************************************************************************

# >>>
# For me, it's: C:\Users\Mr. Louis>python C:\Users\fnde\PycharmProjects\Python-for-Beginners\Module1_Python-Basics\00. introduction.py
