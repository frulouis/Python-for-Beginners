# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : loops.py
# @Software: PyCharm
# @Comments:  Detailed Reading: https://www.datacamp.com/community/tutorials/functions-python-tutorial

# ======================================================================================
# Table Of Content
# Concept 6.1.0: Functions vs Methods
# Concept 6.1.1: How To Define and Call A Function: User-Defined Functions (UDFs)
# Concept 6.1.2: Parameters vs Arguments
# Concept 6.1.3: Default Arguments
# Concept 6.1.4: Required Arguments
# Concept 6.1.5: Keyword Arguments 
# Concept 6.1.6: Variable Number of Arguments
# Concept 6.1.7: Global vs Local Variables
# Concept 6.1.8: Pass by reference vs value
# Concept 6.1.9: The return Statement from functions
# Concept 6.1.10: Anonymous / Lambda Functions in Python
# Concept 6.1.11: The pass Statement
# Concept 6.1.12: Recursion
# ======================================================================================


# **************************************************************************************
# Concept 6.1.0: Functions vs Methods
# **************************************************************************************
# >>>

# A function is a piece of code written to carry out a specified task.
# A method refers to a function which is part of a class. You access it with an instance or object of the class.
# A function doesn’t have this restriction: it just refers to a standalone function.

# Define a function `plus()`
def plus(a, b):
    return a + b


plus(2, 5)

# Create a `Summation` class
class Summation(object):
    def sum(self, a, b):
        self.contents = a + b
        return self.contents

    # Instantiate `Summation` class to call `sum()`

sumInstance = Summation()
sumInstance.sum(1, 2)


# **************************************************************************************
# Concept 6.1.1: How To Define and Call A Function: User-Defined Functions (UDFs)
# **************************************************************************************

# >>>
# Function definition is here
def hello():
    print("Hello World")
    return


# Now you can call hellow function
hello()


# >>>
# Function definition is here
def printme(str):
    # "This prints a passed string into this function"
    print(str)
    return

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


# **************************************************************************************
# Concept 6.1.2: Parameters vs Arguments
# **************************************************************************************
# >>>

# Parameters are the names used when defining a function or a method, and into which arguments will be mapped. In other words, arguments are the things which are supplied to any function or method call, while the function or method code refers to the arguments by their parameter names.

# Function Arguments: You can call a function by using the following types of formal arguments −
# Required arguments
# Keyword arguments
# Default arguments
# Variable-length arguments

# **************************************************************************************
# Concept 6.1.3: Default Arguments
# **************************************************************************************
# >>>

# Define `plus()` function
def plus(a, b=2):
    return a + b

# Call `plus()` with only `a` parameter
plus(a=1)

# Call `plus()` with `a` and `b` parameters
plus(a=1, b=3)

# **************************************************************************************
# Concept 6.1.4: Required Arguments
# **************************************************************************************
# >>>

# Define `plus()` with required arguments
def plus(a, b):
    return a + b

plus(2, 3)

# **************************************************************************************
# Concept 6.1.5: Keyword Arguments  
# **************************************************************************************
# >>>

# Define `plus()` function
def plus(a, b):
    return a + b


# Call `plus()` function with parameters 
plus(2, 3)

# Call `plus()` function with keyword arguments
plus(a=1, b=2)

# Call `plus()` function with keyword arguments
plus(b=2, a=1)


# **************************************************************************************
# Concept 6.1.6: Variable Number of Arguments
# **************************************************************************************
# >>>

# Define `plus()` function to accept a variable number of arguments
def plus(*args):
    return sum(args)


# Calculate the sum
plus(1, 4, 5)

# **************************************************************************************
# Concept 6.1.7: Global vs Local Variables
# **************************************************************************************
# >>>

# Global variable `init`
total = 1

# Define `plus()` function to accept a variable number of arguments
def plus(*args):
    # Local variable `sum()`
    total = 0
    for i in args:
        total += i
    return total


# Access the global variable
print("this is the total value " + str(total))

# (Try to) access the local variable
print("this is the sum " + str(2, 5, 3))


# **************************************************************************************
# Concept 6.1.8: Pass by reference vs value
# **************************************************************************************
# >>>

# Function definition is here
def changeme(mylist):
    #"This changes a passed list into this function"
    mylist.append([1, 2, 3, 4]);
    print("Values inside the function: ", mylist)
    return


# Now you can call changeme function
mylist = [10, 20, 30];
changeme(mylist);
print("Values outside the function: ", mylist)


# **************************************************************************************
# Concept 6.1.9: The return Statement from functions
# **************************************************************************************
# >>>

# Function definition is here
total = 0


def sum(x, y):
    # Add both the parameters and return them."
    total = x + y
    print("Inside the function : ", total)
    return total;


# Now you can call sum function
total = sum(10, 20);
print("Outside the function : ", total)

# **************************************************************************************
# Concept 6.1.10: Anonymous / Lambda Functions in Python
# **************************************************************************************
# >>>

double = lambda x: x * 2

double(5)

# >>>

# `sum()` lambda function
sum = lambda x, y: x + y;

# Call the `sum()` anonymous function
sum(4, 5)

# "Translate" to a UDF
def sum(x, y):
    return x + y


# >>>
from functools import reduce

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use lambda function with `filter()`
filtered_list = list(filter(lambda x: (x * 2 > 10), my_list))

# Use lambda function with `map()`
mapped_list = list(map(lambda x: x * 2, my_list))

# Use lambda function with `reduce()`
reduced_list = reduce(lambda x, y: x + y, my_list)

print(filtered_list)
print(mapped_list)
print(reduced_list)


# **************************************************************************************
# Concept 6.1.11: The pass Statement
# **************************************************************************************
# >>>

def myfunction():
    pass


# **************************************************************************************
# Concept 6.1.12: Recursion
# **************************************************************************************
# >>>

# Python also accepts function recursion, which means a defined function can call itself.

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results")
tri_recursion(6)
