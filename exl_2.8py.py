import turtle
edge=10
turtle.setup(500,500,0,0)
turtle.setup()
for i in range(8):
    turtle.fd(edge)
    turtle.pendown()
    turtle.left(90)
    turtle.fd(edge)
    turtle.left(90)
    edge=edge+10
    turtle.fd(edge)
    turtle.left(90)
    turtle.fd(edge)
    turtle.left(90)
    edge=edge+10
