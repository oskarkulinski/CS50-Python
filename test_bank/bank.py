def main():
    greeting = input('What greeting have you received? ')
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith('hello')==True:
        return 0
    elif greeting.startswith('h')==True:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()