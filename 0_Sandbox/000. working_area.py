# ======================================================================================
# Concept 9.0.6: Raising an Exceptions (Working with Files Example)
# ======================================================================================
# >>>>>>


def check_age(user_age):
    if user_age < 21:
        raise Exception("UnderAge")  # Raise the exception.


age = input("Please enter your age: ")
age = int(age)

try:
    check_age(age)
except Exception:
    print("Verify ID! This person is underage.")
else:
    print("Ready to go! This person is legal age.")
