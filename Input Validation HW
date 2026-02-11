from ast import While


def main():
    hours = int(input("enter hours"))
    minutes = int(input("enter minutes"))
    hours, minutes = validate(hours, minutes)
    print(f'you entered {hours} hours, and {minutes} minutes')


def validate(hr, mins):
    HOURS = 23
    MINUTES = 59

    while hr > HOURS:
        print("hours out of range, enter valid hours")
        hr = int(input('enter hours'))
    while mins > MINUTES:
        print("minutes out of range, enter valid minutes")
        mins = int(input("enter minutes"))
    return hr, mins


main()
