# -*- coding: utf-8 -*-
# @Time    : 2019/11/30 23:13
# @Author  : @frulouis - www.frulouis.com
# @Index   : Access www.threelly.com for indexes of associated video on  YouTube. 
# @File    : loops.py
# @Software: PyCharm
# @Comments:  

# ======================================================================================
# Table Of Content
# Concept 5.1.0: "For" Loop
# Concept 5.1.1: "While" Loop
# Concept 5.1.2: "break" and "continue" statements
# Concept 5.1.3: "else" clause for loop
# Concept 5.1.4: Nested Loops
# Concept 5.1.5: Breaking Loops
# ======================================================================================


# **************************************************************************************
# Concept 5.1.0: "For" Loop
# **************************************************************************************
# >>>
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# >>>	
language = ["Python", "Java", "Ruby"]

for lang in language:
    print("Current language is: ", lang)

    for lang in range(len(language)):
        print("Current language is: ", language[lang])


        # >>>
        # Prints out the numbers 0,1,2,3,4
        for x in range(5):
            print(x)

        # Prints out 3,4,5
        for x in range(3, 6):
            print(x)

        # Prints out 3,5,7
        for x in range(3, 8, 2):
            print(x)

        # **************************************************************************************
        # Concept 5.1.1: "While" Loop
        # **************************************************************************************

        # >>>

        # Prints out 0,1,2,3,4
        count = 0
        while count < 5:
            print(count)
            count += 1  # This is the same as count = count + 1

        # >>>

        # Take user input
        number = 2

        # Condition of the while loop
        while number < 5:
            # Find the mod of 2
            if number % 2 == 0:
                print("The number " + str(number) + " is even")
            else:
                print("The number " + str(number) + " is odd")

            # Increment `number` by 1
            number = number + 1

        # **************************************************************************************
        # Concept 5.1.2: "break" and "continue" statements
        # **************************************************************************************
        # >>>

        # Prints out 0,1,2,3,4
        count = 0
        while True:
            print(count)
            count += 1
            if count >= 5:
                break

        # Prints out only odd numbers - 1,3,5,7,9
        for x in range(10):
            # Check if x is even
            if x % 2 == 0:
                continue
            print(x)

        # **************************************************************************************
        # Concept 5.1.3: "else" clause for loop
        # **************************************************************************************
        # >>>

        # Prints out 0,1,2,3,4 and then it prints "count value reached 5"
        count = 0
        while (count < 5):
            print(count)
            count += 1
        else:
            print("count value reached %d" % (count))

        # Prints out 1,2,3,4
        for i in range(1, 10):
            if (i % 5 == 0):
                break
            print(i)
        else:
            print(
                "this is not printed because for loop is terminated because of break but not due to fail in condition")

        # **************************************************************************************
        # Concept 5.1.4: Nested Loops
        # **************************************************************************************

        # >>>
        # Take user input
        number = 2

        # condition of the while loop
        while number < 5:
            # condition of the nested while loop
            while number % 2 == 0:
                print("The number " + str(number) + " is even")

        # >>>
        # Print the below statement 3 times
        for number in range(3):
            print("-------------------------------------------")
            print("I am outer loop iteration " + str(number))
            # Inner loop
            for another_number in range(5):
                print("****************************")
                print("I am inner loop iteration " + str(another_number))

        # >>>
        # Initialize the first five rows
        n = 10

        # Start the loop to print the first five rows
        for i in range(n):
            for j in range(i):
                print('* ', end="")
            print('')

        # Start the loop to print the remaining rows in decreasing order of stars
        for i in range(n, 0, -1):
            for j in range(_):
                print('* ', end="")
            print('')

        # **************************************************************************************
        # Concept 5.1.5: Breaking Loops
        # **************************************************************************************

        # >>>
        numbers = [0, 254, 2, -1, 3]

        for num in numbers:
            if (num < 0):
                print("Negative number detected!")
                break
            print(num)

        # >>>
        # Print the below statement 3 times
        for number in range(3):
            print("-------------------------------------------")
            print("I am outer loop iteration " + str(number))
            for another_number in range(3):
                print("****************************")
                print("I am inner loop iteration " + str(another_number))
                break
