import turtle
win = turtle.Screen()
t = turtle.Turtle()

for num in range(4):
    t.forward(50)
    t.left(90)

t.penup()
t.backward(200)
t.pendown()

for num in range(4):
    t.forward(100)
    t.left(120)
    
win.mainloop()
