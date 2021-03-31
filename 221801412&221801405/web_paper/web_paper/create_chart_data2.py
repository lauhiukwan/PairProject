from __init__ import *
from models import *
import json

key_list=PaperToKeyword.query.all()
dit=dict()
for k in key_list:
    dit[k.keyword] = dit.get(k.keyword,1)+1
if __name__ == '__main__':
    key_name = list(dit.keys())
    key_value = list(dit.values())
    for i in range(0,10):
        index = i
        max = key_value[i]
        for j in range(i+1,len(key_value)):
            if max<key_value[j]:
                max=key_value[j]
                index=j
        temp=key_value[i]
        key_value[i]=key_value[index]
        key_value[index]=temp
        temp2 = key_name[i]
        key_name[i] = key_name[index]
        key_name[index] = temp2
    f=open('chart2.txt','w')
    f.truncate()
    f.write(str(key_name[0:10])+'\n')
    f.write(str(key_value[0:10]))
    f.close()
    f1 = open('chart2.txt')
    data = f1.readline()
    data2 =f1.readline()
    print(data)
    print(data2)