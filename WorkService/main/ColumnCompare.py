#coding=utf-8 
from numpy import *
from Levenshtein import *
from service.util import *
fr_source=open('../data/compareColumn1')
fr_des=open('../data/compareColumn2')
columns1=[]
columns2=[]

for line1 in fr_source.readlines(): 
    cur_line1=my_split(line1)
    for item1 in cur_line1:
        columns1.append(item1)

for line2 in fr_des.readlines():
    cur_line2=my_split(line2)
    for item2 in cur_line2:
        columns2.append(item2)

class columnsDis:
    columnA=''
    columnB=''
    dis=0

result=[]


for item1 in columns1:
    for item2 in columns2:
        temp=columnsDis()
        temp.columnA=item1
        temp.columnB=item2
        temp.dis=distance(item1,item2)
        result.append(temp)

result.sort(key=lambda x:x.dis, reverse=False)

for item in result:
    if item.columnA in columns1 and item.columnB in columns2:
        print item.columnA+"    "+item.columnB+"    "+str(item.dis)
        columns1.remove(item.columnA)
        columns2.remove(item.columnB)

if len(columns1)==0:
    for item in columns2:
        print "                "+item
        
if len(columns2)==0:
    for item in columns1:
        print item+"                 "