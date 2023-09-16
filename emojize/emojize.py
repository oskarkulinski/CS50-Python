import emoji

text = input("Input: ")

output = emoji.emojize(f"{text}")

print("Output: ", output)