import random

while level <= 0:
    level = input("Level: ")

answer = random.randint(1, level)
while guess != answer:
    