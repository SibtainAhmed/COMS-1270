# Sibtain Ahmed
# Oct 11, 2025
# Lab 7
import random

def generateInput():
    numList = []
    randRange = random.randrange(200, 501)
    for _ in range(randRange):
        numList.append(random.randint(1, 2000))
    return numList


def findMean(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def findMedian(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]
    
def main():
    numbers = generateInput()
    mean = findMean(numbers)
    median = findMedian(numbers)
    print(f"Mean: {mean}")
    print(f"Median: {median}")

if __name__ == "__main__":
    main()