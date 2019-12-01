# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : flow_control.py
# @Software: PyCharm
# @Comments:  Detailed Reading: https://www.datacamp.com/community/tutorials/functions-python-tutorial

# ======================================================================================
# Table Of Content
# 1. Loops ( While, Do while, for )
# Concept 7.1.0: For Loop
# Concept 7.1.1: While loop

# 2. Decision-Making ( if-else)
# Concept 7.1.2: If, Else, Elif

# 3. Exception Handling (Continue, Try-Except, Pass, Break)
# Concept 7.1.3: Break Statement
# Concept 7.1.4: Continue Statement
# Concept 7.1.5: Try Statement
# Concept 7.1.6: Pass Statement
# ======================================================================================


# **************************************************************************************
# Concept 7.1.0: For Loop
# **************************************************************************************
# >>>
# for Loop
fruits = ["apple", "orange", "grapes"]
for fruit in fruits:
    print(fruit)

# **************************************************************************************
# Concept 7.1.1: While loop
# **************************************************************************************

# >>>
a = 5
while a > 1:
    print(a)
    a -= 1

    # >>>
while True:
    print('Please type your name.')
name = input()
if name == 'your name':
    break
print('Thank you!')

# **************************************************************************************
# Concept 7.1.2: If, Else, Elif
# **************************************************************************************
# >>>

a = 10
if a == 0:
    print("Zero")
elif a > 0:
    print("Positive number")
else:
    print("Negative number")

# **************************************************************************************
# Concept 7.1.3: Break Statement
# **************************************************************************************
# >>>

a = 10
while a > 1:
    print(a)
    if a == 5:
        break
    a -= 1

# **************************************************************************************
# Concept 7.1.4: Continue Statement
# **************************************************************************************
# >>>

a = 5
while a > 1:
    if a == 3:
        continue
    print(a)
    a -= 1

# **************************************************************************************
# Concept 7.1.5: Try Statement
# **************************************************************************************
# >>>

try:
    x = int(input("Please input some numbers: "))
    print(x)
except ValueError as ve:
    print("Please input numbers. NUMBERS not letters")

# **************************************************************************************
# Concept 7.1.6: Pass Statement
# **************************************************************************************
# >>>

for letter in 'Python':
    if letter == 'h':
        pass
        print
        'This is pass block'
    print
    'Current Letter :', letter

print
"Good bye!"
