# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : user_inputs.py
# @Software: PyCharm
# @Comments:  

# ======================================================================================
# Full Table Content
# Exercise 1.5.0: #Basic user inputs. Name
# Exercise 1.5.1: #Basic user inputs. Name and age
# Exercise 1.5.2: #Build a basic calculator. Takes two numbers and add them on the screen.
# ======================================================================================

# **************************************************************************************
# Exercise 1.5.0: #Basic user inputs. Name
# **************************************************************************************

# >>>
name = input("Enter your name: ")
print("Hello " + name + "!")

# **************************************************************************************
# Exercise 1.5.1: #Basic user inputs. Name and age
# **************************************************************************************

# >>>
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + " years old!")

# **************************************************************************************
# Exercise 1.5.2: #Build a basic calculator. Takes two numbers and add them on the screen.
# **************************************************************************************

# >>>
num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
result1 = num1 + num2
print(
    "The sum of " + num1 + " and " + num2 + " is  " + result1)  # THIS WOULD FAIL!!!!!! #By default, python inputs are string.

# >>>
result2 = int(num1) + int(num2)  # Cast to int to do addition.
print("The sum of " + num1 + " and " + num2 + " is  " + str(result2))  # Cast to string to display results.

# >>> A better calculator to handle non-integer additions.
result3 = float(num1) + float(num2)  # by default, python inputs are string.
print("The sum of " + num1 + " and " + num2 + " is  " + str(result3))
