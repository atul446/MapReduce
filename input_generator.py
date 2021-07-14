from random import randint
f = open("input1.txt","a")
for i in range(1,10000001):
    s = "" + str(i) + ": "
    nItems = randint(1,50)
    for j in range(nItems):
        item = randint(100,5000)
        s += str(item) + " "
    f.write(s+"\n")
