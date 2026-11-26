import time
import turtle

turtle.shape("turtle")
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

colors = ["purple", "hotpink", "skyblue", "greenyellow", "orange"]

for i in range(72):
    turtle.color(colors[i % len(colors)])
    turtle.circle(110)
    turtle.right(5)

turtle.hideturtle()
time.sleep(5)
