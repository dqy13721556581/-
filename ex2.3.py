turtle

turtle.setup(650,350,200,200)

turtle.penup()

turtle.fd(-100)

turtle.pendown()

turtle.pensize(20)

turtle.pencolor("violet")

turtle.seth(-40)

for i in range(3):

    turtle.circle(40,80)

    turtle.penup()

    turtle.pendown()

    turtle.pencolor("yellow")

    turtle.circle(-40,80)

    turtle.penup()

    turtle.pendown()

    turtle.pencolor("red")

turtle.circle(40,80/2)

turtle.fd(40)

turtle.penup()

turtle.pendown()

turtle.pencolor("blue")

turtle.circle(16,180)

turtle.fd(40*2/3)




