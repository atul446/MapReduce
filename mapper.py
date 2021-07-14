#!/usr/bin/python3
import sys

for line in sys.stdin:
    data = line[0:len(line)-2].split(": ")
    if len(data)==2:
        li = list(map(int, data[1].split(" ")))
        if len(li)>=1 and len(li)<=10:
            classNo = "class1"
        elif len(li)>=11 and len(li)<=20:
            classNo = "class2"
        elif len(li)>=21 and len(li)<=30:
            classNo = "class3"
        elif len(li)>=31 and len(li)<=40:
            classNo = "class4"
        elif len(li)>=41 and len(li)<=50:
            classNo = "class5"
        cost = data[1]
        print ("{0},{1}".format(classNo, cost))
