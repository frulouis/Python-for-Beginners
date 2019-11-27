# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : variables.py
# @Software: PyCharm
# @Comments:  

# ======================================================================================
# Table Of Content
# Concept 1.1.0: Setting and priting variables of different types.
# Concept 1.1.1: Basic variable assignment.
# Concept 1.1.2: Variable Scope - Inside and outside functions.
# Concept 1.1.3: More variable Scope - Inside and outside functions.
# ======================================================================================


# **************************************************************************************
# Concept 1.1.0: Setting and priting variables of different types.
# **************************************************************************************
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

# >>>
my_name = "Fru"  # Python developers by convention like underscores.
my_first_name = "Fru"
my_age = "thirty"
my_age = 30  # Even thou age is same variable name, it's perfectly fine in python as python is dynamically typed. Unlike java.
_my_middleName125 = "Louis"  # This is perfectly fine in python. Starting with underscore. Having non leading digits, e.t.c.

# >>> These are not acceptable. By convention, variable names must be on the right side.
# 30 = my_age
# 6my_name = "Fru"  # Variables cannot start with digits
# class = "Fru"  # python has a who list of reserved words that cannot be used in variable names.

# List of Reserved words in python:
# False	class	finally	is	return
# None	continue	for	lambda	try
# True	def	from	nonlocal	while
# and	del	global	not	with
# as	elif	if	or	yield
# assert	else	import	pass
# break	except	in	raise


# **************************************************************************************
# Concept 1.1.1: Basic variable assignment.
# **************************************************************************************

# >>>: Python allows you to assign values to multiple variables in one line:


first, middle, last = "first", "middle", "last"
print(first)
print(middle)
print(last)

# >>>: Python allows you to assign values to multiple variables in one line:
first = middle = last = "Fru"
print(first)
print(middle)
print(last)

# >>> This is fine too. Even though, data type is different.
first, middle, age = "first", "middle", 30
print(first)
print(middle)
print(last)

# **************************************************************************************
# Concept 1.1.2: Variable Scope - Inside and outside functions.
# **************************************************************************************

# >>>
my_name = "Fru"


def my_greetings():
    print("My name is " + my_name)


my_greetings()

# >>>
my_name = "Fru"


def my_greetings():
    my_name = "Louis"
    print("My name is " + my_name)


my_greetings()

print("My name is " + my_name)

# **************************************************************************************
# Concept 1.1.3: More variable Scope - Inside and outside functions.
# **************************************************************************************

my_name = "Fru"


def my_greetings():
    global my_name
    my_name = "Fru"


my_greetings()

print("My name is " + my_name)
