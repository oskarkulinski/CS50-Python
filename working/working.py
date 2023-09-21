import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hours := re.search(r"(\d):?(\d\d)? ([AP]M) to (\d):?(\d\d)? ([AP]M)",s.strip()):
        if int(hours.group(1)) > 12 or int(hours.group(4)) > 12:
            raise ValueError
        if hours.group(2) != None and hours.group(5) != None:
            if int(hours.group(2)) > 60 or int(hours.group(5)) > 60:
                raise ValueError
            else:
                #start time

                result = convert_hour(1, hours)
                result += ":" + hours.group(2) + " " + hours.group(3)

                result += " to "

                #finish time

                result += convert_hour(4, hours)
                result += ":" + hours.group(5) + " " + hours.group(6)

                return result
        else:
            result = convert_hour(1, hours)
            result += ":00 " + hours.group(3)
            result += " to "
            result += convert_hour(4, hours)
            result += ": " + hours.group(6)

    else:
        raise ValueError


def convert_hour(x, hours):
    if hours.group(x + 2) == "AM" and int(hours.group(x)) < 10:
        result = "0" + hours.group(x)
    elif hours.group(x + 2) == "PM":
            result = str(int(hours.group(x)) + 12)
    else:
        result = hours.group(x)
    return result


if __name__ == "__main__":
    main()