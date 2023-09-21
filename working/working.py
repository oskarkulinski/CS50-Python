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
                result = ""

                #start time

                if hours.group(3) == "AM" and int(hours.group(1)) < 10:
                    result = "0" + hours.group(1)
                elif hours.group(3) == "PM":
                    result = str(int(hours.group(1)) + 12)
                else:
                    result = hours.group(1)
                result += ":" + hours.group(2) + " " + hours.group(3)

                result += " to "

                #finish time

                if hours.group(6) == "AM" and int(hours.group(4)) < 10:
                    result = "0" + hours.group(4)
                elif hours.group(6) == "PM":
                    result = str(int(hours.group(4)) + 12)
                else:
                    result = hours.group(4)
                result += ":" + hours.group(3) + " " + hours.group(6)

                return result
        else:
            


    else:
        raise ValueError


...


if __name__ == "__main__":
    main()