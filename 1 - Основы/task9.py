#!/bin/env python
'''
9. Write a Python program to remove duplicates from a list.
'''

def do(lst):
    H={}; res=[]
    for i in lst:
      if lst[i] not in H:
        H[lst[i]] = 1
        res.append(lst[i])
    return res

print(do([1,2,3,2,5,2,3]))
