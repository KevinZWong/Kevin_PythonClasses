
def PosorNeg(num): 
    if num < 0:
        return "neg"
    if num > 0:
        return "pos"
    


var1 = 1
list1 = []

while var1 != 0:
    if var1 != 0:
        var1 = float(input())
        list1.append(var1)


Pos = []
Neg = []
if list1[0] != 0:
    sum = 0
    list2 = len(list1)-1
    for i in list1:
        sum = sum + i
    average = sum/list2

for i in list1:
    if list1[0] == 0:
        break
    if i != 0:
        result = PosorNeg(i)
        if result == "pos":
            Pos.append(result)
        else:
            Neg.append(result)

if list1[0] != 0:
    print("Average:", average)
    print("Negitive:", len(Neg) )
    print("Positive:", len(Pos) )

if list1[0] == 0:
    print("Average: 0")
    print("Negitive: 0") 
    print("Positive: 0") 
