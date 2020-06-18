import turtle as t
#1.3
print("1.3 \n")
print('FFFFFFF U     U NN    NN')
print('FF      U     U NNN   NN ')
print('FFFFFFF U     U NN N  NN ')
print('FF       U   U  NN  N NN ')
print('FF        UUU   NN   NNN ')

#1.9
width = 4.5
lenth = 7.9
print("The area of the rectangle is ", width * lenth)
print("The permeter of the rectange is", width*2 + lenth*2)

#1.10
print("The runner's speed is", (14*0.6) / (45.5*1.6), "mph /n")

#1.11
TimeSeconds = 360 * 24 * 60 * 60 
birth = TimeSeconds//7
death = TimeSeconds//13
immigrant = TimeSeconds//45
CurrentPopulation = 312032486
print(birth, death, immigrant)

for i in range(1, 6):
    print("After" , i ,"year(s) the populattion will be", CurrentPopulation + birth * i - death * i + immigrant * i )

#1.15
print("1.15 n\ ")
t.pendown()
t.right(120)
for i in range (1, 4):
    t.right(120)
    t.forward(100)
t.right(120)
for i in range (1, 4):
    t.left(120)
    t.forward(100)

