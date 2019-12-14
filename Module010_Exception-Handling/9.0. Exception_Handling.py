# -*- coding: utf-8 -*-
# @Time    : 2019/12/01 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : Exception_Handling.py
# @Software: PyCharm
# @Comments:


# ======================================================================================
# Table Of Content
# Concept 9.0.0: Handling an exception (User Input Example)  
# Concept 9.0.1: Raise Exception (User Input Example)
# Concept 9.0.2: Handling an exception (Working with Files Example) 
# Concept 9.0.3: try...finally  (Working with Files Example) 
# Concept 9.0.4: The except Clause with No Exceptions  (Working with Files Example) 
# Concept 9.0.5: The except Clause with Multiple Exceptions (Working with Files Example) 
# Concept 9.0.6: Raising an Exceptions (Working with Files Example) 
# ======================================================================================

"""""
#An exception is an error that happens during execution of a program. When that
#error occurs, Python generate an exception that can be handled, which avoids your
#program to crash.

IOError
If the file cannot be opened.

ImportError
If python cannot find the module

ValueError
Raised when a built-in operation or function receives an argument that has the
right type but an inappropriate value

KeyboardInterrupt
Raised when the user hits the interrupt key (normally Control-C or Delete)

EOFError
Raised when one of the built-in functions (input() or raw_input()) hits an
end-of-file condition (EOF) without reading any data

Source: https://www.pythonforbeginners.com/error-handling/exception-handling-in-python#:~:targetText=To%20use%20exception%20handling%20in,be%20executed%20statement%20by%20statement.

"""""

# ======================================================================================
# Concept 9.0.0: Handling an exception (User Input Example)
# ======================================================================================
# >>>>>>

# Check the Age of the User
while True:
    try:
        age = input("Please enter your age: ")
        age = int(age)
        break
    except ValueError:
        print("Not a number! Let's try this again ...")
print("Voila! We've got your age as: " + str(age))

# ======================================================================================
# Concept 9.0.1: Raise Exception (User Input Example)
# ======================================================================================
# >>>>>>

while True:
    age = input("Please enter your age: ")

    if not type(int(age)) is int:
        raise TypeError("Only integers are allowed")  # Raise Exception
    else:
        print("Voila! We've got your age as: " + str(age))

# ======================================================================================
# Concept 9.0.2: Handling an exception (Working with Files Example) 
# ======================================================================================
# >>>>>>

try:
    customers = open(
        "C:\\Users\\fnde\\PycharmProjects\\Python-for-Beginners\\Practice_Library\\datasets\\customers1.csv",
        "r+")  # Open file Reading
    print(customers.read())
except IOError:
    print("Error: can not find file or read data. Please try again")
else:
    print("\n CONFIRMATION: The file was read successfully")

# ======================================================================================
# Concept 9.0.3: try...finally  (Working with Files Example) 
# ======================================================================================
# >>>>>>

try:
    customers = open(
        "C:\\Users\\fnde\\PycharmProjects\\Python-for-Beginners\\Practice_Library\\datasets\\customers.csv",
        "r+")  # Open file Reading
    print(customers.read())
except:
    print("Error: can\'t find file or read data. Please try again")
finally:
    print("\n \nCONFIRMATION: The file was read successfully")
    customers.close()

# ======================================================================================
# Concept 9.0.4: The except Clause with No Exceptions  (Working with Files Example) 
# ======================================================================================
# >>>>>>

try:
    customers = open(
        "C:\\Users\\fnde\\PycharmProjects\\Python-for-Beginners\\Practice_Library\\datasets\\customers.csv",
        "r+")  # Open file Reading
    print(customers.read())
except:
    print("Error: can\'t find file or read data. Please try again")
finally:
    print("\n \nCONFIRMATION: The file was read successfully")
    customers.close()

# ======================================================================================
# Concept 9.0.5: The except Clause with Multiple Exceptions (Working with Files Example) 
# ======================================================================================
# >>>>>>

try:
    customers = open(
        "C:\\Users\\fnde\\PycharmProjects\\Python-for-Beginners\\Practice_Library\\datasets\\customers1.csv",
        "r+")  # Open file Reading
    print(customers.read().strip())
except (IOError, ValueError):
    print("An I/O error or a ValueError occurred")
except:
    print("An unexpected error occurred")
    raise


# ======================================================================================
# Concept 9.0.6: Raising an Exceptions (Working with Files Example) 
# ======================================================================================
# >>>>>>


def check_age(user_age):
    if user_age < 21:
        raise ("Under Age!" + str(user_age))  # Raise the exception.


age = input("Please enter your age: ")
age = int(age)

try:
    check_age(age)
except "Under Age!":
    print("Verify ID! This person is underage.")
else:
    print("Ready to go! This person is legal age.")
