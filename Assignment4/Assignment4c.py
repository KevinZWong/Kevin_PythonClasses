print("4.8")
list1 = []
print("Enter 3 numbers: number1,number2,number3")
var1 = input()
list1 = var1.split(",")
for i in range(0, 3, 1):
    list1[i] = int(list1[i])
print("Your numbers in increasing order are:", sorted(list1))
