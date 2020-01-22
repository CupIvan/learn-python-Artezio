#!/bin/env python
'''
2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

print('Print string: ')
S=input()
H={}
for char in S:
    H[char] = H.get(char, 0) + 1
print(H)
