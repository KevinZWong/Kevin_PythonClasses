import time
import random as r
print("5.2")
t0= time.perf_counter()

correct = 0
incorrect = 0
for i in range(0,10,1):
        
    ran1 = r.randrange(1, 15)
    ran2 = r.randrange(1, 15)
    answer = ran1 + ran2
    if answer < 0:
        ran1, ran2 = ran2, ran1
    answer = ran1 + ran2
    print(ran1 ,"+", ran2 ,"=")
    var1 = int(input())


    if var1 == answer:
        print("Correct")
        correct += 1
    elif var1 != answer:
        print("Incorrect, the correct answer was", answer)
        incorrect += 1
print("############################")
print("Incorrect:", incorrect)
print("Correct:", correct)
t1 = time.perf_counter() - t0
print("Time elapsed:", int(t1 * 100)//100.0, "seconds" ) # CPU seconds elapsed (floating point)