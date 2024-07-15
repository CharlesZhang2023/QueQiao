# This Script is used to provide a GUI to generate waypoints for Egoplanner and save them.
import turtle
import math
from hover import *


# Initalize Map and Grid
screen = turtle.Screen()
screen.setup(width=800, height=800)

def draw_grid():
    grid_turtle = turtle.Turtle()
    grid_turtle.speed(0)
    turtle.tracer(False)
    grid_turtle.penup()
    grid_turtle.hideturtle()

    grid_turtle.color(0.9, 0.9, 0.9)
    for x in range(-400, 401, 20):
        grid_turtle.goto(x, -400)
        grid_turtle.pendown()
        grid_turtle.goto(x, 400)
        grid_turtle.penup()

    for y in range(-400, 401, 20):
        grid_turtle.goto(-400, y)
        grid_turtle.pendown()
        grid_turtle.goto(400, y)
        grid_turtle.penup()

    grid_turtle.pensize(2)
    grid_turtle.pencolor(0.6,0.6,0.6)

    # X-axis
    grid_turtle.goto(-400, 0)
    grid_turtle.pendown()
    grid_turtle.goto(400, 0)
    grid_turtle.penup()

    # Y-axis
    grid_turtle.goto(0, -400)
    grid_turtle.pendown()
    grid_turtle.goto(0, 400)
    grid_turtle.penup()
    turtle.update()
    turtle.tracer(True)

draw_grid()




# Define Fast waypoint generation function
t = turtle.Turtle()
t.penup()

waypoints = []


def goto_click(x, y):
    t.penup()
    current_x, current_y = t.pos()
    angle = math.degrees(math.atan2(y - current_y, x - current_x))
    t.setheading(angle)
    
    t.goto(x, y)
    waypoints.append((x, y))

screen.onscreenclick(goto_click)

def move_forward():
    t.forward(20)

def turn_left():    
    t.left(20)

def turn_right():
    t.right(15)


# Go back to home position
def go_home():
    goto_click(0, 0)
    # t.penup()
    # t.goto(0, 0)
    # t.pendown()

# Circle Around 
def circle_around():
    current_x, current_y = t.pos()
    current_heading = t.heading()
    #t.forward(50)
    circle_center_x, circle_center_y = t.pos()
    t.rt(90)
    for i in range(1):
        t.circle(60)
    

    #waypoints.append("Circle around")
    t.goto(current_x, current_y)
    pos = (current_x+math.cos(math.radians(current_heading))*60, current_y+math.sin(math.radians(current_heading))*60)
    logging=waypoint_generate(pos, current_heading-180, 60, 6)
    waypoints.extend(logging)
    t.setheading(current_heading)
    t.pendown()
    
# Circle and return
def explore():
    circle_around()
    go_home()
    
# Quit program and save waypoints to file
def quit_program():
    print("Flight logging:")
    for waypoint in waypoints:
        print(waypoint)
    
    with open("./waypoints.txt", "w") as f:
        for waypoint in waypoints:
            f.write(str(waypoint) + "\n")

    print("Waypoints saved to waypoints.txt.")
    print("Successful flight.")
    screen.bye()

# Bind keys to functions
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(quit_program, "q")
screen.onkey(go_home,"h")
screen.onkey(circle_around,"c")
screen.onkey(explore,"e")

# Start program
screen.mainloop()

