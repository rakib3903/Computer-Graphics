
import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Flag of Bangladesh")
screen.bgcolor("white")

# Create turtle
t = turtle.Turtle()
t.speed(0)


# Flag dimensions
flag_width = 300
flag_height = 180

# Colors
green = "#006a4e"
red = "#f42a41"

# Draw green rectangle (flag background)
t.penup()
t.goto(-flag_width/2, flag_height/2)
t.color(green)
t.begin_fill()
for _ in range(2):
    t.forward(flag_width)
    t.right(90)
    t.forward(flag_height)
    t.right(90)
t.end_fill()

# Draw red circle (disk)
circle_radius = 60
circle_center_x = - 30
circle_center_y = 0

t.goto(circle_center_x, -circle_radius)
t.setheading(0)
t.color(red)
t.begin_fill()
t.circle(circle_radius)
t.end_fill()

t.penup()
t.goto(-flag_width/2, flag_height/2)
t.color("silver")
t.begin_fill()

t.backward(10)
t.right(90)
t.forward(500)
t.left(90)

t.forward(10)
t.left(90)
t.forward(500)
    
t.end_fill()
# Hide turtle and finish
t.hideturtle()
screen.mainloop()
