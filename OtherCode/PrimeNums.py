
def PrimeYN(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            return number

def PrimeRange(var1):
    list1 = []
    for i in range(1, var1 + 1, 1):
        result = PrimeYN(i)
        if (result != None):
            list1.append(result)
    return list1
            
var1 = int(input())
var1 = var1//2
list1 = PrimeRange(var1)
print(list1)