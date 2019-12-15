"""
This simple program Converst money from one currency to another. (USD to XAF and USD to NGN)
Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
Bonus: Expand your program to work and support exchange between any other currency, in the world. 

"""


def dollar_to_xaf():
    user_value = input("How many dollars? ")
    ammount = float(user_value)
    conversion = ammount * 0.26
    print(str(user_value) + " dollars is equal to " + str(conversion) + " dollars.")


def dollar_to_ngn():
    pass


print("Welcome to currency converter.")
print("Supported currencies: Central African Francs (XAF) and Niara (NGN)")

user_choice1 = input("Convert: ")
user_choice2 = input("To: ")

if user_choice1 == "USD" and user_choice2 == "XAF":
    dollar_to_xaf()

elif user_choice1 == "USD" and user_choice2 == "NGN":
    dollar_to_ngn()
