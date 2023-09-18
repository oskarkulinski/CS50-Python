def main():
    text = input('What do you want to say? ')
    print(shorten(text))


def shorten(word):
    shortened = ""
    for x in text:
        if x =='a' or x=='e' or x == 'i' or x == 'o' or x == 'u' or x=='A' or x=='E' or x=='I' or x == 'O' or x == 'U':
            continue
        else:
            shortened += x


if __name__ == "__main__":
    main()