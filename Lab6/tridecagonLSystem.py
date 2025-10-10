# Sibtain Ahmed
# using Runestone 9.15.2 as reference


from Lab3.tridecagonTurtle import tridecagonTurtle

import random

import turtle




def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F++H-FP'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'H':
            tridecagonTurtle(distance, aTurtle.xcor(), aTurtle.ycor() ,  aTurtle)
        elif cmd == 'P':
            aTurtle.penup()
            aTurtle.goto(random.randint(-200,200), random.randint(-200,200))
            aTurtle.pendown()

def main():
    initialStr = input("Enter the initial string (axiom): ")
    inst = createLSystem(4, initialStr) 
    print(inst)
    t = turtle.Turtle()        
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    angle = int(input("Enter the angle: "))
    sideLength = int(input("Enter the side length: "))
    drawLsystem(t, inst, angle, sideLength) 
                             
    wn.exitonclick()

main()
