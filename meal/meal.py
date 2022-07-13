def main():
    hour = input('What time is it? ')
    convert(hour)
    if 7 <= result <= 8:
        print('breakfast time')
    elif 12 <= result <= 13:
        print('lunch time')
    elif 18 <= result <=19:
        print('dinner time')


def convert(time):
    hr, min = time.split(sep=':')
    hr = float(hr)
    min = float(min)/60
    result = hr + min
    return result

main()