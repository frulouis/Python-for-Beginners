# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : bitwise.py
# @Software: PyCharm
# @Comments:  

# ======================================================================================
# Full Table Content
# Exercise 2.6.0: #Bitwise Operators
# ======================================================================================


# **************************************************************************************
# Exercise 2.6.0: #Bitwise Operators
# **************************************************************************************

# >>>
a = 10
b = 35

print(a & b)  # AND	Sets each bit to 1 if both bits are 1

print(a | b)  # OR	Sets each bit to 1 if one of two bits is 1

print(a ^ b)  # XOR	Sets each bit to 1 if only one of two bits is 1

print(~a)  # NOT	Inverts all the bits

print(a << 2)  # Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off

print(
    a >> b)  # Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
