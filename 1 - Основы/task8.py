#!/bin/env python
'''
8. Write a Python program to find the highest 3 values in a dictionary
'''

def highest3(d1):
    return sorted(d1.values())[-3:]

print(highest3({1:2,3:8}))
print(highest3({1:2,3:8,5:4,7:6}))
print(highest3({1:2,3:8,5:4,7:6,'a':4,'b':7}))
