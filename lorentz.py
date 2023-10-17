import turtle
window = turtle.Screen()
turtle.setup(600, 600)
turtle.setworldcoordinates(-24, -80, 26, 80)
turtle.bgcolor("black")

t = turtle.Turtle(shape="circle")
t.shapesize(0.6 , 0.6 , 0.6)
t.color("orange")
t.width(0)

turtle.tracer(25, 0)

dt = 0.001
sigma = 10.0
rho = 27.0
beta = 8.0 / 3.0

x, y, z = 0.5, 0.1, 0.5

if __name__ == "__main__":

    for i in range(100000):
        x += dt * sigma * (y - x)
        y += dt * (x * (rho - z) -y)
        z += dt * (x * y - beta * z)

        t.goto(x, z)



