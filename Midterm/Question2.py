import turtle as t
def drawLine(x1,y1,x2,y2,color,size):
    t.pencolor(str(color))
    t.pensize(int(size))
    t.penup()
    t.goto (x1,y1)
    t.pendown()
    t.goto(x2,y2)

def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))

sides = input("Enter a 3 side: x1,y1,x2,y2,x3,y3: ")
list1 = []
list1 = sides.split(",")


for i in range(0,6,1):
    list1[i] = int(list1[i])


result = triangle_area(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5])
t.pencolor("black")
t.pensize(3)
t.penup()
t.goto (0,-300)
t.pendown()
t.write("Area = ")
t.goto (40,-300)
t.write(result)

drawLine(list1[0],list1[1],list1[2],list1[3],"black",3)
t.write((list1[2],list1[3]), True)
drawLine(list1[2],list1[3],list1[4],list1[5],"black",3)
t.write((list1[4],list1[5]), True)
drawLine(list1[4],list1[5],list1[0],list1[1],"black",3)
t.write((list1[0],list1[1]), True)
t.done()


