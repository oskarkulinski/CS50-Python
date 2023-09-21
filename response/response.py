from validator_collection import validators, checkers, errors

text = input("What's your email address? ")

if checkers.is_email(text) == True:
    print("Valid")
else:
    print("Invalid")
