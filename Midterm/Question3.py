WIDTH = 10
HEIGHT = 5

def In_X_axis(x):
    if (x < WIDTH / 2):
        return True
    else:
        return False

def In_Y_axis(y):
    if (y < HEIGHT / 2):
        return True
    else:
        return False

x1  = float(input("Input X: "))
InX = In_X_axis(x1)
y1 = float(input("Input Y: "))
InY = In_Y_axis(y1)

if (InX and InY):
    print("The point is inside")
else:
    print("The point is outside")