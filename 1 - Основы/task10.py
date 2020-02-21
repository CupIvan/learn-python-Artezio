#!/bin/env python
'''
10. Write a Python program to get the difference between the two lists
'''

def do(lst1, lst2):
    return list(set(lst1) - set(lst2))

print(do([1,2,3,2,5,2,3],[2,3,2,6]))
