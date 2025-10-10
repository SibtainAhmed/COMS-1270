# Sibtain Ahmed     09-13-2024


from random import randrange

def randomProduct(a,b,c):
    resultant = 1
    for _ in range(a):
        resultant *= randrange(b, c+1)
    return resultant


def main():
    a = int(input("Please input a positive integer 'a': "))
    b = int(input("Please input a positive integer 'b': "))
    c = int(input("Please input a positive integer 'c' where c>b: "))
    answer = randomProduct(a,b,c)
    print(f"Product of {a} random number = {answer}")


if __name__ == "__main__":
    main()