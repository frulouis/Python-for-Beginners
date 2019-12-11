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
# Concept 7.1.5: Try-Except Statement
# Concept 7.1.6: Pass Statement
# ======================================================================================


# **************************************************************************************
# Concept 7.1.0: For Loop
# **************************************************************************************
# >>>
# for Loop
my_names = ["coach", "fru", "louis", "nde"]
for name in my_names:
    print(name)

# **************************************************************************************
# Concept 7.1.1: While loop
# **************************************************************************************

# >>>
age = 30
while age > 1:
    print(age)
    age -= 1

# >>>
while True:
    name = input('Please type your name.')
    if name == 'Fru':
        print("Fru is not allowed.")
        break
print('Thank you! Your name is: ' + name)

# **************************************************************************************
# Concept 7.1.2: If, Else, Elif
# **************************************************************************************
# >>>

age = 30
if age == 0:
    print("Zero")
elif age > 0:
    print("Positive number")
else:
    print("Negative number")

# **************************************************************************************
# Concept 7.1.3: Break Statement
# **************************************************************************************
# >>>

age = 30
while age > 1:
    print(age)
    if age == 21:
        print("Legal age starts here.")
        break
    age -= 1

# **************************************************************************************
# Concept 7.1.4: Continue Statement
# **************************************************************************************
# >>>

age = 30
while 30 > 1:
    if age == 21:
        continue
    print(age)
    age -= 1

# **************************************************************************************
# Concept 7.1.5: Try Statement
# **************************************************************************************
# >>>

try:
    age = int(input("Please input your age: "))
    print(age)
except ValueError as ve:
    print("Please input your age in NUMBERS not letters!")

# **************************************************************************************
# Concept 7.1.6: Pass Statement
# **************************************************************************************
# >>>

print('Printing my name and url horizontally \n')

for curr_value in 'Coach Fru Louis on YouTube (www.threelly.com)':
    if curr_value == 'F':
        pass  # The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
        print('My actual name begins here:')
    print(curr_value)

print("\nThere you go! My name and url in horizontal.")
