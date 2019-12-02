# -*- coding: utf-8 -*-
# @Time    : 2019/12/01 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : File_Operations.py
# @Software: PyCharm
# @Comments:


# ======================================================================================
# Table Of Content
# Concept 8.0.0: Basic IO Operations on .txt file (Read, Write, Append, e.t.c)
# Concept 8.0.1: Operating System (OS) and Directory Commands in Python. 
# ======================================================================================


# ======================================================================================
# Concept 8.0.0: Basic IO Operations on .txt file (Read, Write, Append, e.t.c)
# ======================================================================================
# >>>>>>


"""""
File Modes in Python
Mode	Description
'r'	This is the default mode. It Opens file for reading.
'w'	This Mode Opens file for writing. If file does not exist, it creates a new file.  If file exists it truncates the file.
'x'	Creates a new file. If file already exists, the operation fails.
'a'	Open file in append mode. If file does not exist, it creates a new file.
't'	This is the default mode. It opens in text mode.
'b'	This opens in binary mode.
'+'	This will open a file for reading and writing (updating)
"""""

# >>>
# Read .csv file
customers = open("C:\\Users\\fnde\\PycharmProjects\\Python-for-Beginners\\Practice_Library\\datasets\\customers.csv",
                 "r+")  # Open file Reading

print(customers.read())

customers.close()  # Close file

# >>>
# (Over) Write .csv file
customers = open("C:\\Users\\fnde\\PycharmProjects\\Python-for-Beginners\\Practice_Library\\datasets\\customers.csv",
                 "w+")  # Open file Write
for i in range(21, 30):
    print(i)
    customers.write("\n" + str(i) + ",Heinrick,McOwan,hmcowank@dailymail.co.uk,Male")  # Write in the file

print(customers.read())

customers.close()  # Close file

# >>>
# (Append) Write .csv file
customers = open("C:\\Users\\fnde\\PycharmProjects\\Python-for-Beginners\\Practice_Library\\datasets\\customers.csv",
                 "a+")  # Open file Append
for i in range(21, 30):
    print(i)
    customers.write("\n" + str(i) + ",Heinrick,McOwan,hmcowank@dailymail.co.uk,Male")  # Write in the file

print(customers.read())

customers.close()  # Close file

# ======================================================================================
# Concept 8.0.1: Operating System (OS) and Directory Commands in Python. 
# ======================================================================================
# >>>>>>

import os

##########   DIRECTORY OPERATIONS
# Check current directory location

current_dir = os.getcwd()
print(current_dir)

# >>>
# Set Current directory
os.chdir('C:\\Users\\fnde\\PycharmProjects\\Python-for-Beginners\\Practice_Library\\datasets\\')
print(os.getcwd())

# >>>
# List Directory
print(os.listdir(os.getcwd()))

# >>>
# Create New Directory
os.mkdir('demo_dir')

os.chdir('C:\\Users\\fnde\\PycharmProjects\\Python-for-Beginners\\Practice_Library\\datasets\\demo_dir')

##########  FILE OPERATIONS

# >>>
# File Operations #RENAME
os.rename("customers_pickle.csv", "customers_pickle2.csv")
print(os.listdir(os.getcwd()))

# >>>
# File Operations #DELETE
os.remove("customers_pickle2.csv")
