from validator_collection import checkers

text = input("What's your email address? ")

if is_email(text) == True:
    print("Valid")
else:
    print("Invalid")
