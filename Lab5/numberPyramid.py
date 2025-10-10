# Sibtain Ahmed
# Date: 09-27-2025
# Lab 5

def numberPyramid(n):
    for i in range(1, n + 1):
        # print(' ' * (n - i), end='')
        for _ in range(n - i):
            print(' ', end='')
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


def main():
    n = int(input("Enter the number of rows for the number pyramid: "))
    numberPyramid(n)

if __name__ == "__main__":
    main()