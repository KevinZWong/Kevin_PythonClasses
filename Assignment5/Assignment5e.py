def calFactorial(num):
    factorial = 1

    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
        return 1
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        #print("The factorial of",num,"is",factorial) 
        return factorial


def funct1(var1):
    # this is the 1 +
    sum = 1 
    # To start with 1, and end with "var1 + 1", but not included; default step: 1
    for j in range(1, var1 + 1):  
        # To add 1 term at a time
        sum = sum + 1/calFactorial(j)
        #print("sum= ", sum)

    # To print out the answer
    print("sum= ", sum)


list1 = [10000,20000,30000,100000]
for var1 in list1:
    funct1(var1)

