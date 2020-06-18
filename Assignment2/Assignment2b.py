print("2.13")
print("Enter a 4-digit number:")
OriginalNum = int(input())

First = int(OriginalNum/1000)
Second = int(OriginalNum/100)
Third = int(OriginalNum/10)
Fourth = int(OriginalNum/1)
print(First)
print(Second - First*10)
print(Third - First*100 - (Second - First*10)*10)
Third = Third - First*100 - (Second - First*10)*10
print(Fourth - First*1000 - (Third* 10) - (Second - First*10)*100)


