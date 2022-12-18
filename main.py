print("<-----RULES----->\n1. BRUSH DOWN\n2. BRUSH UP\n3. VEHICLE ROTATES RIGHT\n4. VEHICLE ROTATES LEFT\n5. MOVE UP TO X\n6. JUMP\n7. REVERSE DIRECTION\n8. VIEW THE MATRIX\n0. EXIT")
n = input("Please enter the commands with a plus sign (+) between them.\n").split("+")
list = []

for i in n:
    if int(i) >= 0:
        list.append(i)
z=int(list[0])
list.pop(0)
y=True

while y==True:
    for r in list:
        if r!=list[0]:
            if int(r) >= 9 or int(r) <= -1:
                if r[:1] != str(5):
                    print("You entered an incorrect command. Please try again!")
                    n = input("Please enter the commands with a plus sign (+) between them.\n").split("+")
                    list = []
                    for i in n:
                        if int(i) >= 0:
                            list.append(i)
                    z = int(list[0])
                    list.pop(0)
                    y=True
        else:
            y=False
            continue

matrix = [['+' for x in range(z + 2)] for y in range(z + 2)]
for j in range(1, z + 1):
    for i in range(1, z + 1):
        matrix[j][i] = " "

x=1         #COORDINATE
y=1         #COORDINATE
cd=1        #CARSDIRECTION 1=RIGHT 2=DOWN 3=LEFT 4=UP
k =0        #X IN 5_X
bd=False    #BRUSHDOWN

for r in list:

    if int(r) == 1:#BRUSH UP AND BRUSH DOWN COMMANDS--------
        bd = True
        matrix[x].pop(y)
        matrix[x].insert(y, '*')
    elif int(r) == 2:
        bd = False

    if len(r)>=3 and r[:1]== str(5):#MOVE UP TO X COMMANDS---
        k = r[2:]
        k = int(k)
        if bd == True and cd == 1:
            for k in range(1, k + 1):
                if y==z:
                    y = 1
                    matrix[x].pop(y)
                    matrix[x].insert(y, '*')
                    k=k-1
                elif y!=z:
                    y = y + 1
                    matrix[x].pop(y)
                    matrix[x].insert(y, '*')
                    k=k-1
        elif bd == True and cd == 2:
            for k in range(1, k + 1):
                if x==z:
                    x=1
                    matrix[x].pop(y)
                    matrix[x].insert(y, '*')
                elif x != z:
                    x = x + 1
                    matrix[x].pop(y)
                    matrix[x].insert(y, '*')
        elif bd == True and cd == 3:
            for k in range(1, k + 1):
                if y==1:
                    y=z
                    matrix[x].pop(y)
                    matrix[x].insert(y, '*')
                elif y != 1:
                    y = y - 1
                    matrix[x].pop(y)
                    matrix[x].insert(y, '*')
        elif bd == True and cd == 4:
            for k in range(1, k + 1):
                if x==1:
                    x=z
                    matrix[x].pop(y)
                    matrix[x].insert(y, '*')
                elif x != 1:
                    x = x - 1
                    matrix[x].pop(y)
                    matrix[x].insert(y, '*')
        elif bd == False and cd == 1:
            for k in range(1, k + 1):
                if y==z:
                    y = y - z + 1
                elif y != z:
                    y = y + 1
        elif bd == False and cd == 2:
            for k in range(1, k + 1):
                if x==z:
                    x=1
                elif x != z:
                    x = x + 1
        elif bd == False and cd == 3:
            for k in range(1, k + 1):
                if y==1:
                    y=z
                elif y != 1:
                    y = y - 1
        elif bd == False and cd == 4:
            for k in range(1, k + 1):
                if x==1:
                    x=z
                elif x != 1:
                    x = x - 1

    if int(r) == 3:#TURN RIGHT AND TRUN LEFT COMMANDS---
        if cd == 4:
            cd = cd-3
        elif cd == 1 or cd == 2 or cd == 3:
            cd = cd + 1
    if int(r) == 4:
        if cd == 1:
            cd = 4
        elif cd == 4 or cd == 2 or cd == 3:
            cd = cd - 1

    if int(r) == 6:#JUMP COMMANDS-------------------------
        bd = False
        if cd == 1:
            for i in range(1, 4):
                y = y + 1
        elif cd == 2:
            for i in range(1,4):
                x = x + 1
        elif cd == 3:
            for i in range(1, 4):
                y = y - 1
        elif cd == 4:
            for i in range(1, 4):
                x = x - 1

    if int(r) == 7:#REVERSE DIRECTION COMMAND------------
        if cd == 1 or cd == 2:
            cd = cd + 2
        else:
            cd = cd - 2

    if int(r) == 8:#VİEW THE MATRİX COMMAND--------------
        for y in matrix:
            print(*y,sep='')

    if int(r) == 0:#END PROGRAM COMMAND------------------
        break
    k=0