# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : loops.py
# @Software: PyCharm
# @Comments:  Detailed Reading: https://www.datacamp.com/community/tutorials/functions-python-tutorial

# ======================================================================================
# Table Of Content
# Concept 8.1.0: Defining a Class
# ======================================================================================


# Overview of OOP Terminology: https://www.tutorialspoint.com/python/python_classes_objects.htm


# **************************************************************************************
# Concept 8.1.0: Defining a Class
# Concept 8.1.1: Class Inheritance
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

# test code
print(car1.description())
print(car2.description())


# **************************************************************************************
# Concept 8.1.1: Class Inheritance
# **************************************************************************************
# Class Inheritance : https://www.tutorialspoint.com/python/python_classes_objects.htm
# >>>

class Parent:  # define parent class
    parentAttr = 100

    def __init__(self):
        print
        "Calling parent constructor"

    def parentMethod(self):
        print
        'Calling parent method'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print
        "Parent attribute :", Parent.parentAttr


class Child(Parent):  # define child class
    def __init__(self):
        print
        "Calling child constructor"

    def childMethod(self):
        print
        'Calling child method'


c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
c.setAttr(200)  # again call parent's method
c.getAttr()  # again call parent's method
