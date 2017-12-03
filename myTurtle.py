import turtle

my_turtle =turtle.Turtle()

def square(n,m):
   
    my_turtle.forward(n)
    my_turtle.right(m)
    my_turtle.forward(n)
    my_turtle.right(m)
    my_turtle.forward(n)
    my_turtle.right(m)
    my_turtle.forward(n)

for i in range(15):
    square(20,10)

fruits = ['Apple','banana','jackfruit']
fruits

