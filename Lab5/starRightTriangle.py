# Sibtain Ahmed
# Date: 09-27-2025
# Lab 5

def starRightTriangle(n):
    for i in range(1, n + 1):
        print('*' * i)


def main():
    n = int(input("Enter the number of rows for the right triangle: "))
    starRightTriangle(n)

if __name__ == "__main__":
    main()