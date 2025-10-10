

def findLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def main():
    year = int(input("Enter a year: "))
    answer = findLeapYear(year)
    if answer:
        print(f"Yes, {year} is a leap year.")
    else:
        print(f"No, {year} is not a leap year.")

if __name__ == "__main__":
    main()