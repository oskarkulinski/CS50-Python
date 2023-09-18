def main():
    text = input('What do you want to say? ')
    print(shorten(text))


def shorten(word):
    shortened = ""
    for c in word:
        if c =='a' or c =='e' or c == 'i' or c == 'o' or c == 'u' or c =='A' or c =='E' or c =='I' or c == 'O' or c == 'U':
            continue
        else:
            shortened = shortened + c
    return shortened

if __name__ == "__main__":
    main()