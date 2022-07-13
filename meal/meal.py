def main():
    hour = input('What time is it? ')
    convert(hour)
    if 7 < hour < 8:
        print('breakfast time')
    

def convert(time):
    hr, min = time.split(sep=':')
    hr = float(hr)
    min = float(min)/60
    time = hr + min


if __name__ == "__main__":
    main()