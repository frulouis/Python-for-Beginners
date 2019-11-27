# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : numbers.py
# @Software: PyCharm
# @Comments:  

# ======================================================================================
# Full Table Content
# Exercise 1.2.0: #Basic numbers
# Exercise 1.2.1: #Number types and how to check them: Int, Float, Complex
# Exercise 1.2.2: #Numbers and Arithmetic operations
# Exercise 1.2.3: #BODMAS - Order of operation
# Exercise 1.2.4: #More math functions in python
# Exercise 1.2.5: #Converting numbers from one type to another
# Exercise 1.2.6: #Printing Random Numbers
# ======================================================================================


# Importing External Libraries
from math import *
from random import *

# **************************************************************************************
# Exercise 1.2.0: #Basic numbers
# **************************************************************************************

# >>>
print(3)  # Integers
print(3.124)  # Doubles / Decimals
print(-3.124)  # Signed Values

# **************************************************************************************
# Exercise 1.2.1: #Number types and how to check them: Int, Float, Complex
# **************************************************************************************

# >>>
x = 5  # int
y = 7.8  # float
z = 3j  # complex
print(type(x))
print(type(y))
print(type(z))

# **************************************************************************************
# Exercise 1.2.2: #Numbers and Arithmetic operations
# **************************************************************************************

# >>>
print(3 + 2.5)  # Addition
print(3 - 2.5)  # Subtraction
print(3 / 2.5)  # Division
print(3 * 2.5)  # Multiplication
print(3 % 2)  # Modulus

# **************************************************************************************
# Exercise 1.2.3: #BODMAS - Order of operation
# **************************************************************************************

# >>>
print(3 * 2 + 5)  # Modulus - 11
print(3 * (2 + 5))  # Modulus - 21

# **************************************************************************************
# Exercise 1.2.4: #More math functions in python
# **************************************************************************************

# >>>
my_age = -30
print(my_age)
print(abs(my_age))
print("My age is " + str(my_age) + ".")
print(pow(5, 2))  # raising power
print(max(5, 2, 35, 8))  # find max
print(min(5, 2, 35, 8))  # find min
print(round(5.57))  # round to integer => 6
print(round(5.47))  # round to integer => 5
print(floor(5.47))  # round to integer => 5  #IMPORT library/module:  from math import *
print(ceil(5.47))
print(sqrt(25))

# **************************************************************************************
# Exercise 1.2.5: #Converting numbers from one type to another
# **************************************************************************************

# >>>
x = 1  # int
y = 2.8  # float
z = 1j  # complex
a = float(x)  # convert from int to float:
b = int(y)  # convert from float to int:
c = complex(x)  # convert from int to complex:
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# **************************************************************************************
# Exercise 1.2.6: #Print Random Numbers
# **************************************************************************************
print(random.randrange(1, 10))
