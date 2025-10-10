# Sibtain Ahmed
# Week 4 Lab

from turtle import Turtle

def drawMultipleTridecagons(s, x, y, nr, sr, t):
    for i in range(nr):
        tridecagonTurtle(s, x + i*sr, y, t)
    

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
    nr = int(input("Please input number of tridecagons: "))
    sr = int(input("Please input spacing between tridecagons: "))
    # Turtle.screen()
    t = Turtle()

    drawMultipleTridecagons(s, x, y, nr, sr, t)
    t.screen.exitOnClick()


if __name__ == "__main__":
    main()