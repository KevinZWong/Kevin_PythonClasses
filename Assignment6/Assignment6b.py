# Return true if point (x2, y2) is on the left side of the
# directed line from (x0, y0) to (x1, y1)
def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    result = (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)
    if result > 0:
        return True
    else:
        return False

def leftOfTheLine2(x0, y0, x1, y1, x2, y2):
    result = (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)
    if result < 0:
        return True
    else:
        return False

# Return true if point (x2, y2) is on the same
# line from (x0, y0) to (x1, y1)
def onTheSameLine(x0, y0, x1, y1, x2, y2):
    result = (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)
    if result == 0:
        return True
    else:
        return False



# Return true if point (x2, y2) is on the
# line segment from (x0, y0) to (x1, y1)
def onTheLineSegment(x0, y0, x1, y1, x2, y2):
    return onTheSameLine(x0,y0,x1,y1,x2,y2) and min(x0, x1) <= x2 <= max(x0, x1) and min(y0, y1) <= y2 <= max(y0, y1)


def First():
    points = input("Enter points: x0,y0,x1,y1,x2,y2: " )
    list1 = points.split(",")

    for i in range(0,len(list1),1):
        list1[i] = float(list1[i])


    Lresult = leftOfTheLine(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5])
    if Lresult:
        print("Point 3 is on the left side of the line")

    Lresult = leftOfTheLine2(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5])
    if Lresult:
        print("Point 3 is on the right side of the line")

    Sresult = onTheLineSegment(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5])
    if Sresult:
        print("Point 3 is on the line segment")
        exit()
        
    Oresult = onTheSameLine(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5])
    if Oresult:
        print("Point 3 is on the same line")
First()

