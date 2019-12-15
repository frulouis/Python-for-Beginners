# Write a program, where given two numbers a and b, the program will check if a is a power of b. e.g.
# 25, 5 : TRUE
# 10, 2 : FALSE

# Key Concepts: FUNCTIONS, RECURSION***, VARIABLES, PRINTING, STRINGS,

# Pseudo-Code (check if a is a power of b) 1, 10
# 1.) a%b == 0  ==> 4%2 == 0   TRUE  #Check Divisible
# 2.) a/b == power of b  ==> 4/2 = 2 (is 2 a power of 2) TRUE.  #Check is Power.

# lambda
l_divisible = lambda x, y: x % y == 0


# regular
def f_divisible(x, y):
    return x % y == 0


def is_power(a, b):
    if a == 1 or b == 1:
        return True
    else:
        return l_divisible(a, b) and is_power((a / b), b)  # Recursion


# Printing some test results.
print("power(1, 10): " + str(is_power(1, 10)))
print("power(10, 1): " + str(is_power(10, 1)))
print("power(10, 2): " + str(is_power(10, 2)))
print("power(25, 3): " + str(is_power(25, 3)))
print("power(25, 5): " + str(is_power(25, 5)))
print("power(5641851541515151515151250, 5): " + str(is_power(5641851541515151515151250, 5)))
