print("5.26")
list1 = []
for i in range(1,100,1):
    if i % 2 != 0:
        list1.append(i)


sum = 0
for i in range(0, len(list1) - 1,1):
    sum += list1[i] / list1[i+1]

   # answer = sun + answer
print("sum= ", sum)


#45



























'''print("5.26")
answer = 0
list1 = []
for i in range(1,110,1):
    if i % 2 != 0:
        list1.append(i)
print(list1)

for i in range(0,17,1):
    var1 = (list1[0]/list1[1]) + (list1[1]/list1[2])
    print((list1[0], "/" ,list1[1]), "+" ,(list1[1], "/" ,list1[2])) 
    list1.pop(0)
    list1.pop(0)
    list1.pop(0)
    answer = answer + var1
answer = answer - (99/101)
print(answer)
        

'''
#30
