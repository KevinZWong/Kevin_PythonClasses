##drawing a star
import turtle as t
    
def drawLine(x1,y1,x2,y2,color,size):
    t.pencolor(str(color))
    t.pensize(int(size))
    t.penup()
    t.goto (x1,y1)
    t.pendown()
    t.goto(x2,y2)

t.color("black")
t.speed(10)
drawLine(300,-400,0,400,"black",3)
drawLine(300,-400,-500,100,"black",3)
drawLine(-500,100,500,100,"black",3)
drawLine(500,100,-300,-400,"black",3)
drawLine(-300,-400,0,400,"black",3)
t.done()