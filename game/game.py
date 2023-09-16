import random

level = 0
guess = 0

while level <= 0:
    level = int(input("Level: "))

answer = random.randint(1, level)
while guess != answer:
    guess = int(input("Guess: "))
    if guess < answer:
        print("Too small!")
    elif guess > answer:
        print("Too large!")

print("Just right!")