print("5.10")
list1 = []
#inputs
var1 = 0

while var1 != 0:

    var1 = int(input())
    list1.append(var1)




for i in range(0, 3, 1):
    list1[i] = int(list1[i])
print("Your numbers in increasing order are:", sorted(list1))
