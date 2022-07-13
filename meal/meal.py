def main():
    hour = input('What time is it? ')
    convert(hour)
    if 7 <= hour <= 8:
        print('breakfast time')
    elif 12 <= hour <= 13:
        print('lunch time')
    elif 18 <= hour <=19:
        print('dinner time')


def convert(time):
    hr, min = time.split(sep=':')
    hr = float(hr)
    min = float(min)/60
    time = float(hr + min)
    return time

main()