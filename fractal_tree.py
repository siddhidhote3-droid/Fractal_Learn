import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Fractal Tree - Fractal_Learn")

# Turtle setup
t = turtle.Turtle()
t.color("green")
t.speed(0)
t.left(90)          # Face upwards
t.penup()
t.goto(0, -250)     # Start from bottom
t.pendown()

# Fractal tree function
def draw_tree(branch_length, level):
    if level == 0:
        return

    t.forward(branch_length)

    t.left(30)
    draw_tree(branch_length * 0.7, level - 1)

    t.right(60)
    draw_tree(branch_length * 0.7, level - 1)

    t.left(30)
    t.backward(branch_length)

# Call the function
draw_tree(120, 6)

turtle.done()
