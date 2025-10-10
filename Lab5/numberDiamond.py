# Sibtain Ahmed
# Date: 09-27-2025
# Lab 5

def numberDiamond(n):
    for i in range(1, n + 1):    
        space = n - i
        for s in range(space):
            print(" ", end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(n - 1, 0, -1):
        space = n - i
        for s in range(space):
            print(" ", end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    n = int(input("Enter an odd number between 1 and 9 for the diamond size: "))
    numberDiamond(n)


if __name__ == "__main__":
    main()