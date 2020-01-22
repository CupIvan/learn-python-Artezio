#!/bin/env python
'''
7. Write a Python script to merge two Python dictionaries
'''

def merge(d1, d2):
    d1.update(d2)
    return d1

print(merge({1:2,3:4}, {'a':'b','c':'d'}))
