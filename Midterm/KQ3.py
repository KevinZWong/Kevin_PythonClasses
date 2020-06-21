sides = input("Enter a point: x1,y1: ")
list1 = []
list1 = sides.split(",")
list1[0] = float(list1[0])
list1[1] = float(list1[1])
if list1[0] > -5 and list1[0] < 5 or list1[0] == -5 or list1[0] == 5:
    xinside = "Yes"
else: 
    xinside = "No"

if list1[1] > -2.5 and list1[1] < 2.5 or list1[1] == -2.5 or list1[1] == 2.5:
    yinside = "Yes"
else: 
    yinside = "No"

if xinside == "Yes" and yinside == "Yes":
    print("The point is inside the box")
else:
    print("The point is outside the box.")

