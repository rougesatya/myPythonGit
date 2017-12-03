import turtle

my_turtle=turtle.Turtle()
my_turtle.speed(5)

def square(length,angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

for i in range(50):
    square(100,90)
    my_turtle.right(11)
my_turtle.forward(200)
for i in range(50):
    square(100,90)
    my_turtle.left(7)

