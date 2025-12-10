import turtle

screen = turtle.Screen()
screen.title("Straight Track - Car Icon")
screen.setup(width=533, height=800)
screen.bgpic("track_straight.png")

car = turtle.Turtle()
car.penup()

screen.addshape("car.gif")   
car.shape("car.gif")      

car.pensize(2)
car.color("red")

path = []
y_start = -250
y_end = 380
step = 10

y = y_start
while y <= y_end:
    path.append((0, y))
    y += step

car.goto(path[0][0], path[0][1])
car.pendown()

car.speed(2)

for point in path[1:]:
    car.goto(point[0], point[1])

turtle.done()
