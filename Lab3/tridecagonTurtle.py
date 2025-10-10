# Sibtain Ahmed
# Week 4 Lab

from turtle import Turtle

def tridecagonTurtle(s,x,y,t):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for _ in range(13):
        t.forward(s)
        t.right(180-152.3)



def main():
    s = int(input("Please input s: "))
    x = int(input("Please input x: "))
    y = int(input("Please input y: "))
    t = Turtle()
    tridecagonTurtle(s,x,y,t)
    # answer = tridecagonTurtle(s, x, y)
    # print(f"Approximated square root of {x} in {iterations} iterations = {answer}")
    t.screen.mainloop()


if __name__ == "__main__":
    main()