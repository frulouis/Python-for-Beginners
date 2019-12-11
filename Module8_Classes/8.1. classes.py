# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : classes.py
# @Software: PyCharm
# @Comments:  Detailed Reading: https://www.datacamp.com/community/tutorials/functions-python-tutorial

# ======================================================================================
# Table Of Content (OOP)
# Concept 8.1.0: Defining a Class
# Concept 8.1.1: Class Inheritance
# Concept 8.1.2: Importing/Using Libraries in Python
# ======================================================================================


# Overview of OOP Terminology: https://www.tutorialspoint.com/python/python_classes_objects.htm

# Classes (OOP) In object-oriented programming, a class is a blueprint for creating objects (a particular data structure),
# providing initial values for state (member variables or attributes), and implementations of behavior
# (member functions or methods). The user-defined objects are created using the class keyword.
# Object.
# Class.
# Method.
# Inheritance.
# Polymorphism.
# Data Abstraction.
# Encapsulation.


# **************************************************************************************
# Concept 8.1.0: Defining a Class
# **************************************************************************************
# >>>

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# your code goes here
car1 = Vehicle()
car1.name = "Toyota"
car2 = Vehicle()
car2.name = "Honda"

# test code
print(car1.description())
print(car2.description())


# **************************************************************************************
# Concept 8.1.1: Class Inheritance
# **************************************************************************************
# Class Inheritance : https://www.tutorialspoint.com/python/python_classes_objects.htm
# >>>

class Parent:  # define parent class
    parentName = "Mother"

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setName(self, name):
        Parent.parentName = name

    def getName(self):
        print("Parent Name :", Parent.parentName)


class Child(Parent):  # define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
c.setAttr(200)  # again call parent's method
c.getAttr()  # again call parent's method

# **************************************************************************************
# Concept 8.1.2: Importing in Python
# **************************************************************************************
# >>>
# External libraries are used with the import [libname] keyword. You can also use from [libname]
# import [funcname] for individual functions. Here is an example:

import random

randomint = random.randint(1, 100)
print(randomint)

64
