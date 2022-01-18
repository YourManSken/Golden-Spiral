import turtle
turtle.speed(0)

scale = 20

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

def spiral(steps):
    f1 = 1
    f2 = 0
    for _ in range(steps):
        temp = f2
        f2 += f1
        f1 = temp
        square(f2*scale)
        turtle.circle(f2*scale, 90)

turtle.right(90)
spiral(8)

turtle.exitonclick()