
input1 = [1, -3, 5, 7, -9, 11]

positive_count = 0
negative_count = 0
total = 0

num = 1
while num != 0:
    num  = int(input("Input a number: "))
    # print("inputed number: ", num)
    if num == 0:
        break
    elif num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    total += num

print("positive_count = ", positive_count)
print("negative_count = ", negative_count)
print("total = ", total)
if (positive_count + negative_count != 0):
    print("average = ", total / (positive_count + negative_count))
else:
    print("No input captured, So, No average ")