import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('tan')
t = turtle.Turtle()

t.pencolor('blue')
t.penup()
t.goto(-80,15)
t.pendown()
t.circle(35)
t.penup()

t.pencolor('red')
t.goto(80,15)
t.pendown()
t.circle(35)
t.penup()

t.pencolor('black')
t.goto(0,15)
t.pendown()
t.circle(35)
t.penup()

t.goto(-40,-15)
t.pencolor('yellow')
t.pendown()
t.circle(35)
t.penup()

t.goto(40,-15)
t.pencolor('green')
t.pendown()
t.circle(35)

t.penup()
t.goto(-125,100)
t.pencolor("purple")
t.pendown()


t.write("Winter Olympics",font=("Arial",30,"bold"))

t.penup()
t.goto(-40,-100)
t.pencolor('purple')
t.pendown()


t.write("2026",font=("Arial",30,"bold"))