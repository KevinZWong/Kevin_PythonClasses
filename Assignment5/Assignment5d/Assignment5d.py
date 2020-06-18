f = open("score.txt", "r")
str1 = f.read()
list5 = str1.split()

Names = []
lenth = len(list5)
lenth2 = lenth//2

for i in range(0, lenth, 2):
    Names.append(list5[i])
for i in range(0,lenth2, 1):
    list5.pop(i)
test_keys = list5
test_values = Names
res = {} 
for key in test_keys: 
    for value in test_values: 
        res[key] = value 
        test_values.remove(value) 
        break  
print("Number of students:", len(list5))

for i in range(0, lenth2, 1):
    list5[i] = int(list5[i])
list5 = sorted(list5)
list5 = list5[::-1]
print("The person with the highest score is", res[str(list5[0])], "with a score of", list5[0])



