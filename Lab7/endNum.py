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

def endNum(intList,  num):
    s = 0
    e = len(intList) - 1
    while s <= e:
        while intList[s] == num:
            intList[s] = intList[e]
            intList[e] = num
            e -= 1
        s += 1
    return intList

def main():
    integers = takeIntegerList()
    num = int(input("Enter the integer to move to the end: "))
    result = endNum(integers, num)
    print("Modified list:", result)

if __name__ == "__main__":
    main()