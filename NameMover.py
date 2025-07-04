import turtle
import time


screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=800, height=400)
screen.title("Smooth Name Scroll")
screen.tracer(0)


writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")
writer.goto(-400, 0)
writer.write("Rakib", font=("Arial", 24, "bold"))
x = -400
while True:
    writer.clear()
    writer.goto(x, 0)
    writer.write("Rakib", font=("Arial", 24, "bold"))
    x += 2
    if x > 400:
        x = -400
    screen.update()
    time.sleep(0.01)
