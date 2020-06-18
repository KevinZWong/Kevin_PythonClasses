

def displayPattern(lenth):
    var1 = 0
    first = [0]
    print(first)
    while var1 != lenth:
        list1 = []
        for i in range(0, var1+2, 1):
            list1.append(i)
        print(list1)
        var1 = var1 + 1



displayPattern(20)
