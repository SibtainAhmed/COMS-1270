# Sibtain Ahmed


def sqrtIter(x,iterations):
    y = 1
    for _ in range(iterations):
        y = ((x/y)+y)/2
    return y


def main():
    x = int(input("Please input x: "))
    iterations = int(input("Please input no of iterations: "))
    answer = sqrtIter(x, iterations)
    print(f"Approximated square root of {x} in {iterations} iterations = {answer}")


if __name__ == "__main__":
    main()