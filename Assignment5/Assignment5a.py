import math 
print("5.18")
def primeFactors(n): 
    list1 = []
    while n % 2 == 0: 
        list1.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n))+1, 2): 
        while n % i == 0: 
            list1.append(i)
            n = n / i 
    if n > 2: 
        list1.append(n) 
    return list1

###########################################################
print("Enter a number:")
n = int(input())
result = primeFactors(n) 
print(result)
