def main():
    face = input('What do you want to say? ')
    face = faces(face)
    print(face)

def faces(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

main()
