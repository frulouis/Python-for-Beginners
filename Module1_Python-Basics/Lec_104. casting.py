# -*- coding: utf-8 -*-
# @Time    : 2019/11/26 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : casting.py
# @Software: PyCharm
# @Comments:  

# ======================================================================================
# Table Of Content
# Concept 1.4.0: #Experiecing data type mismatch
# Concept 1.4.1: #Casting to Int
# Concept 1.4.2: #Casting to Float
# Concept 1.4.3: #Casting to String
# ======================================================================================


# **************************************************************************************
# Concept 1.4.0: #Experiecing data type mismatch
# **************************************************************************************

# >>>
salary = 900
tip = "300"
print(x + y)  # This fails. As the data types are not thesame.

# Common datatypes in python are int(), float() and str(). We'd see more of them below.


# **************************************************************************************
# Concept 1.4.1: #Casting to Int
# **************************************************************************************

# >>>
salary = int(900)  # salary will be 900
tip = int(299.98)  # tips will be 300 #notice the rounding.!!!
bonus = int("70")  # bonus will be 70
print(x + y + z)  # Since datatypes have been converted to match, this should work.

# **************************************************************************************
# Concept 1.4.2: #Casting to Float
# **************************************************************************************

# >>>
salary = float(900)  # salary  will be 900
tip = float(562.7)  # tip will be 562.7
bonus = float("300")  # bonus will be 300
allowance = float("-45.2")  # allowance will be -45.2

# **************************************************************************************
# Concept 1.4.3: #Casting to String
# **************************************************************************************

# >>>
guest_comment = str("awesome service")  # guest_comment will be 'awesome service'
tip = str(252)  # tip will be '252'
bonus = str(332.0)  # bonus will be '332.0'
