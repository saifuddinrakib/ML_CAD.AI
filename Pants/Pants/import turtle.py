import turtle

# define function to draw square
def draw_square():
    # create turtle object
    t = turtle.Turtle()

    # set pen color and fill color
    t.pencolor("black")
    t.fillcolor("green")

    # begin filling the square
    t.begin_fill()

    # draw square
    for i in range(4):
        t.forward(200) # length of the square
        t.right(90)

    # end filling the square
    t.end_fill()

    # hide the turtle object
    t.hideturtle()

    # return turtle object
    return t

# create turtle object
t = draw_square()

# divide square into four equal parts
for i in range(4):
    t.forward(100) # half the length of the square
    t.right(90)
    t.penup()
    t.forward(100) # half the length of the square
    t.pendown()
    t.right(90)

# erase one part from the square
t.begin_fill()
for i in range(4):
    if i == 1: # erase second part
        t.penup()
        t.forward(100) # half the length of the square
        t.right(90)
        t.forward(100) # half the length of the square
        t.left(90)
        t.pendown()
        t.fillcolor("white")
    else:
        t.forward(100) # half the length of the square
        t.right(90)
        t.forward(100) # half the length of the square
        t.left(90)
t.end_fill()

# distribute remaining area among three children
area = 1666.6666666666667
each_child_area = area/3

# calculate half-square distance
half_square_distance = (each_child_area/2)**0.5

# draw lines from half-square points to position where you can easily calculate 3 equal squares
t.penup()
t.goto(0, 100) # start from top-left corner
t.pendown()
t.right(90)
t.forward(half_square_distance)
t.right(90)
t.forward(200*half_square_distance)
t.right(90)
t.forward(half_square_distance)
t.right(90)
t.forward(half_square_distance)
t.right(90)
t.forward(200*half_square_distance)
t.right(90)
t.forward(half_square_distance)

# keep the window open until closed manually
turtle.done()

