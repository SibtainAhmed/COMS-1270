# Sibtain Ahmed
# Date: 09-27-2025
# Lab 5

def sameNumberTriangle(n):
    for i in range(1, n + 1):
        print(f'{i}  ' * i)
    # for i in range(1, n + 1):
    #     for j in range(i):
    #         print(i, end='  ')
        print()
def main():
    n = int(input("Enter the number of rows for the same number triangle: "))
    triangle = sameNumberTriangle(n)
    

if __name__ == "__main__":
    main()