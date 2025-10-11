# Sibtain Ahmed
# Oct 11, 2025
# Lab 7

def takeIntegerList():
    intList = []
    while True:
        userInput = input("Enter an integer (or '*' to finish): ")
        if userInput == '*':
            break
        number = int(userInput)
        intList.append(number)
    return intList

def rotateList(intList, rot):
    n = len(intList)
    if n == 0:
        return intList
    rot = rot % n 
    return intList[-rot:] + intList[:-rot]


def main():
    integers = takeIntegerList()
    rot = int(input("Enter the number of positions to rotate: "))
    result = rotateList(integers, rot)
    print("Rotated list:", result)


if __name__ == "__main__":
    main()