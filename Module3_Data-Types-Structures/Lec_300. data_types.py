# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : arithmetic_operators.py
# @Software: PyCharm
# @Comments:  

# ======================================================================================
# Table Of Content
# Concept 3.0.1: #Numbers
# Concept 3.0.2: #Strings
# Concept 3.0.3: #Boolean
# Concept 3.0.4: #Lists
# Concept 3.0.5: #Tuples
# Concept 3.0.6: #Dictionaries
# Concept 3.0.7: #Frozenset
# Concept 3.0.8: #bytes
# Concept 3.0.9: #	bytearray
# Concept 3.0.10: #	memoryview
# ======================================================================================

"""
There are eight native datatypes in Python.
Boolean
Numbers
Strings
Bytes & Byte Arrays
Lists
Tuples
Sets
Dictionaries
"""

# **************************************************************************************
# Concept 3.0.1: #Numbers
# **************************************************************************************

num1 = 5 ** 3
num2 = 32 // 3
num3 = 32 / 3
print('num1 is', num1)
print('num2 is', num2)
print('num3 is', num3)


# **************************************************************************************
# Concept 3.0.2: #Strings
# **************************************************************************************
str1 = "Welcome"
str2 = " Fru's Coach Academy"
str3 = str1 + str2
print('You are in ', str3)
print(str3[0:10])
print(str3[-5:])
print(str3[:-5])

# **************************************************************************************
# Concept 3.0.3: #Boolean
# **************************************************************************************
number = [1, 2, 3, 4, 5]
boolean = 3 in number
print(boolean)

# **************************************************************************************
# Concept 3.0.4: #Lists
# **************************************************************************************
countries = ['Cameroon', 'Britain', 'United States', 'Canada', 'Spain']
print(len(countries))
print(countries)
countries.append('Nigeria')
print(countries)
countries.insert(2, 'France')
print(countries)

# **************************************************************************************
# Concept 3.0.5: #Tuples
# ************************************************************************************** 
fruits_tuple = ("apple", "banana", "cherry")
fruits_list = list(sports_tuple)
fruits_list.append('orange')
print(fruits_list)
print(fruits_tuple)

# **************************************************************************************
# Concept 3.0.6: #Dictionaries
# **************************************************************************************
# My Fruits at meals
Meals = {'Breakfast': 'apple', 'Lunch': 'banana', 'Dinner': 'cherry'}
print('The fruits I had at meals are ', Meals)
# Modifying for meals
Meals['Breakfast'] = 'Pear'
Meals['Lunch'] = 'Plum'
print('During Meals I have ', Meals)

# **************************************************************************************
# Concept 3.0.7: #Frozenset
# **************************************************************************************
# Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of frozen set remains the same after creation.
vowels = frozenset({('a', 'e', 'i', 'o', 'u')})
vSet = frozenset(vowels)
print('The frozen set is:', vSet)

# **************************************************************************************
# Concept 3.0.8: #bytes
# **************************************************************************************
x = b"Hello"
print(x)

# **************************************************************************************
# Concept 3.0.9: #	bytearray
# **************************************************************************************
x = bytearray(5)
print(x)

# **************************************************************************************
# Concept 3.0.10: #	memoryview
# **************************************************************************************
x = memoryview(bytes(5))
print(x)
