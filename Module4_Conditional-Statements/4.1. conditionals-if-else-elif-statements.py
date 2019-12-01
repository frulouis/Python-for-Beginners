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
total = 100
# country = "US"
country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
    print("Shipping Cost is $25")
elif total <= 150:
    print("Shipping Costs $5")
else:
    print("FREE")
if country == "AU":
    if total <= 50:
        print("Shipping Cost is  $100")
else:
    print("FREE")
