import random

level = 0
guess = 0

while level <= 0:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue

answer = random.randint(1, level)
while guess != answer:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess < answer:
        print("Too small!")
    elif guess > answer:
        print("Too large!")

print("Just right!")