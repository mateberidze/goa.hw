import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
house_pen = turtle.Turtle()
house_pen.speed(2)

# Function to draw a rectangle with a given color
def draw_rectangle(color, width, height):
    house_pen.begin_fill()
    house_pen.fillcolor(color)
    for _ in range(2):
        house_pen.forward(width)
        house_pen.left(90)
        house_pen.forward(height)
        house_pen.left(90)
    house_pen.end_fill()

# Function to draw a triangle with a given color
def draw_triangle(color, size):
    house_pen.begin_fill()
    house_pen.fillcolor(color)
    for _ in range(3):
        house_pen.forward(size)
        house_pen.left(120)
    house_pen.end_fill()

# Draw the purple walls
draw_rectangle("purple", 150, 100)

# Position for the first brown window
house_pen.penup()
house_pen.goto(40, 60)
house_pen.pendown()

# Draw the first brown window
draw_rectangle("brown", 30, 30)

# Position for the second brown window
house_pen.penup()
house_pen.goto(80, 60)
house_pen.pendown()

# Draw the second brown window
draw_rectangle("brown", 30, 30)

# Position for the red roof     
house_pen.penup()
house_pen.goto(0, 100)
house_pen.pendown()

# Draw the red roof
draw_triangle("red", 150)

# Position for the yellow door
house_pen.penup()
house_pen.goto(60, 0)
house_pen.pendown()

# Draw the yellow door
draw_rectangle("yellow", 30, 60)

# Hide the turtle
house_pen.hideturtle()

# Keep the window open
turtle.mainloop()