#!/bin/env python
'''
4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

print('Print strings: ')
S=input()
N=0
A=S.split(' ')
for string in A:
    if len(string) >= 2:
        if string[0] == string[-1]:
            N += 1
print(N)