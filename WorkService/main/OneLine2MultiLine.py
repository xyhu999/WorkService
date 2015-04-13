#coding=utf-8 
from numpy import *
fr = open('../data/oneline2multiline')
splitchar=','          #可更改
for line in fr.readlines():
    lines=line.strip().split(splitchar)
    for item in lines:
        print item.strip()
