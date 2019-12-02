# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : conditionals_if_else_elif_statements.py
# @Software: PyCharm
# @Comments:  
# if expression
# Statement
# else
# Statement

# ======================================================================================
# Table Of Content
# Concept 4.0.1: #If Statement
# Concept 4.0.2: #"else condition"
# Concept 4.0.3: #"else condition" does not work
# Concept 4.0.4: #"elif" condition
# Concept 4.0.5: #conditional statements with minimal code
# Concept 4.0.6: #Nested IF Statement
# ======================================================================================


# **************************************************************************************
# Concept 4.0.1: #If Statement
# **************************************************************************************
# >>>
x, y = 2, 8

if (x < y):
    st = "x is less than y"
print(st)

# **************************************************************************************
# Concept 4.0.2: #"else condition"
# **************************************************************************************
# >>>	
x, y = 8, 4

if (x < y):
    st = "x is less than y"
else:
    st = "x is greater than y"
print(st)

# **************************************************************************************
# Concept 4.0.3: #"else condition" does not work
# **************************************************************************************
# >>>	
x, y = 8, 8

if (x < y):
    st = "x is less than y"
else:
    st = "x is greater than y"
print(st)

# **************************************************************************************
# Concept 4.0.4: #"elif" condition
# **************************************************************************************
# >>>	
x, y = 8, 8

if (x < y):
    st = "x is less than y"

elif (x == y):
    st = "x is same as y"

else:
    st = "x is greater than y"
print(st)

# **************************************************************************************
# Concept 4.0.5: #conditional statements with minimal code
# **************************************************************************************
# >>>	
x, y = 10, 8
st = "x is less than y" if (x < y) else "x is greater than or equal to y"
print(st)

# **************************************************************************************
# Concept 4.0.6: #Nested IF Statement
# **************************************************************************************
# >>>
gpa_total = 2.5
student_name = "John"
Enrolled = "False"

if Enrolled == "True":
    if student_name == "John":
        if gpa_total >= 3.0:
            print("CONGRATS John! You are ready to graduate")
        elif gpa_total >= 1.0:
            print("GPA in fail range. More courses needed. ")
        else:
            print("Sorry John! GPA too low for graduation.")
    else:
        print("HMMMMM :( Not John! Access not allowed.")
else:
    print("Hmmm : You are not currently enrolled. Talk to Admissions.")
