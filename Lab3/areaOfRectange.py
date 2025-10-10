# Sibtain Ahmed         (09-13-2024)
# Lab Week 3 -          This example does something


def areaOfRectangle(height, width):
    # Citation: Area of rectangle is the region occupied by a rectangle within its four sides or boundaries.
    # Citation URL: https://byjus.com/maths/area-of-rectangle/
    # Citation Author:  Someone
    # Citation date:    (date when I accessed above website)
    return height * width


def main():
    height = int(input("Enter height of Rectangle: "))
    width = int(input("Enter width of Rectangle: "))
    answer = areaOfRectangle(height, width)
    print(f"Area of Rectangle = {answer}")

if __name__ == "__main__":
    main()