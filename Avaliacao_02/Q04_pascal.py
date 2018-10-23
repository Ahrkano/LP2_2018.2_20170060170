
# coding: utf-8

from contextlib import redirect_stdout

def pascal_triangle(row):
    list=[1]

    for i in range(row):
        print(list)
        newlist=[]
        newlist.append(list[0])
        for i in range(len(list)-1):
            newlist.append(list[i]+list[i+1])
        newlist.append(list[-1])
        list=newlist
        
with open("triangle.out", "w", encoding="utf-8") as out:
        with redirect_stdout(out):
            print(pascal_triangle(200))

