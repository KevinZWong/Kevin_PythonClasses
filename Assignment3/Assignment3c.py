print("3.5")
import math
print("3.5")
print("Enter the number of sides")
side_Num = float(input())
print("Enter side lenth:")
side = float(input())
area = (side_Num * (side**2)) / (4 * (math.tan(math.pi/side_Num)))

print("The area of the polygon is", area)




