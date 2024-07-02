# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:15:00 2024

@author: Neehar
"""

l=list(map(int,input("Enter the list of numbers: ").split()))
k=int(input("Enter value of K: "))
i,count,j=0,0,len(l)-1
while(k>0):
    if(l[i]>l[j]):
        count+=l[i]
        i+=1
    else:
        count+=l[j]
        j-=1
    k-=1
print(count)