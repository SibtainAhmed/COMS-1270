# Sibtain Ahmed             09-07-2025
# Lab Week 2  -  This code draw initials of my name "SA" on screen with different background and letter colors.
from turtle import Turtle

t = Turtle()

# t.screen.title('CS-1270 Lab#2 Demo')

t.screen.bgcolor("yellow")
t.speed(2)

t.color('green')
t.pensize(20)

t.penup()
t.goto(-50, 100)
t.pendown()

t.back(100)
t.right(90)
t.fd(100)
t.left(90)
t.fd(100)
t.right(90)
t.fd(100)
t.right(90)
t.fd(100)


t.penup()
t.goto(50, -100)
t.pendown()

t.pencolor('red')

t.right(90)
t.fd(200)
t.right(90)
t.fd(100)
t.right(90)
t.fd(200)
t.back(100)
t.right(90)
t.fd(100)


t.screen.mainloop()