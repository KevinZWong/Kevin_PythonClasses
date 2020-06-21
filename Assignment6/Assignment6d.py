#how many prime
print("Enter a number:")
def PrimeYN(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            return number

var1 = int(input())

list1 = []
for i in range(1, var1 + 1, 1):
    result = PrimeYN(i)
    if (result != None):
        list1.append(result)
print(len(list1))