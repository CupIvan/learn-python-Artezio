#!/bin/env python
'''
5. You are given with 3 sets, find if third set is a subset of the first and the second sets
Input: set([1,2]), set([3,4), set([2])
Expected result: True
Input: set([1,2]), set([3,4), set([5])
Expected result: False
'''

def test(need, s1, s2, s3):
    res = s3.issubset(s1.union(s2))
    print('OK' if res == need else 'FAIL')

test(True,  set([1,2]), set([3,4]), set([2]))
test(False, set([1,2]), set([3,4]), set([5]))
