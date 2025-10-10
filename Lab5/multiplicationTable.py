# Sibtain Ahmed
# Date: 09-27-2025
# Lab 5

def multiplicationTable(lowNum, highNum):
    for i in range(lowNum, highNum + 1):
        for j in range(1,11):
            print(repr(i * j).rjust(4), end=" ")
        print()



def main():
    lowNum = int(input("Enter the lower bound (lowNum): "))
    highNum = int(input("Enter the upper bound (highNum): "))

    
    multiplicationTable(lowNum, highNum)
    

if __name__ == "__main__":
    main()