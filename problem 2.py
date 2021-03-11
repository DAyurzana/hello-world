import turtle

user_color = input("Choose the color  ")
Duke = turtle.Turtle()
Duke.pencolor(user_color)

for number in range (4):
    Duke.forward(200)
    Duke.right(90)

turtle.done()
