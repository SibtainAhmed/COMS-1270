# Sibtain Ahmed
# Oct 11, 2025
# Lab 7


def takeStringInputs():
    res = []
    while True:
        element = input("Enter a number (or '*' to finish): ")
        if element == '*':
            break
        else:
            res.append(element)
    return res

def findMin(numList):
    minVal = float('inf')
    for num in numList:
        val = num
        if val < minVal:
            minVal = val
    return minVal

def findMax(numList):
    maxVal = float('-inf')
    for num in numList:
        val = num
        if val > maxVal:
            maxVal = val
    return maxVal 

def main():
    string_num = takeStringInputs()
    numbers = []
    for i in string_num:
        numbers.append(int(i))

    minimum = findMin(numbers)
    maximum = findMax(numbers)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

if __name__ == "__main__":
    main()