
print("Enter three sides of triangle: ") 
a = int(input())
b = int(input())
c = int(input()) 
if ((a + b > c) and (a + c > b) and (b + c > a)):
    print("Triangle is valid, the permeter is", (a + b + c)) 
else : 
    print("Triangle is not valid.")
