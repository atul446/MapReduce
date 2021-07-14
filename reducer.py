#!/usr/bin/python3
import sys


sales_total = [0,0,0,0,0]
key = ['class1','class2','class3','class4','class5']

for line in sys.stdin:
    data = line.strip().split(",")
    data1 = list(map(int,data[1].split(" ")))
    if len(data)!=2:
        continue
    if data[0]==key[0]:
        sales_total[0]+=sum(data1)
    elif data[0]==key[1]:
        sales_total[1]+=sum(data1)
    elif data[0]==key[2]:
        sales_total[2]+=sum(data1)
    elif data[0]==key[3]:
        sales_total[3]+=sum(data1)
    elif data[0]==key[4]:
        sales_total[4]+=sum(data1)

if key!=None:
    for i in range(5):
        print ("{0}, {1}".format(key[i],sales_total[i]))
