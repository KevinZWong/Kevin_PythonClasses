print("3.11")
def KSplit(OriginalNum):
    list1 = []
    First = int(OriginalNum/1000)
    Second = int(OriginalNum/100)
    Third = int(OriginalNum/10)
    Fourth = int(OriginalNum/1)
    list1.append(First)
    list1.append(Second - First*10)
    list1.append(Third - First*100 - (Second - First*10)*10)
    Third = Third - First*100 - (Second - First*10)*10
    list1.append(Fourth - First*1000 - (Third* 10) - (Second - First*10)*100)
    
    return list1

var1 = int(input())
result = KSplit(var1)
result = result[::-1]
print("Your Number backwards is:")
for i in result: 
    print(i, end="") 

