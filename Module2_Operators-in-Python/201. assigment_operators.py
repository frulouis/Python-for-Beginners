# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : assignment_operators.py
# @Software: PyCharm
# @Comments:  

# ======================================================================================
# Full Table Content
# Exercise 2.1.0: #Assignment Operators
# ======================================================================================


# **************************************************************************************
# Exercise 2.1.0: #Assignment Operators
# **************************************************************************************

# >>>
a = 2

b = 5

a = b

print(a)

a += b  # Same as  a + b
print(a)  # adding two numbers and setting result to a

a -= b  # Same as  a - b
print(a)  # subtracting two numbers and setting result to a

a *= b
print(a)  # multiplying two numbers and setting result to a

a /= b
print(a)  # dividing two numbers and setting result to a

a %= b  # modulus two numbers and setting result to a
print(a)

a **= b  # same as 2*2*2*2*2
print(a)

a &= b  # Same as  a & b
print(a)

a |= b
print(a)

a ^= b
print(a)

a >>= b
print(a)

a <<= a
print(a)

a //= b  # the floor division // rounds the result down to the nearest whole number
print(a)
