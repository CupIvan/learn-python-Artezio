#!/bin/env python
'''
2. Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’
'''

def f(a,b,c):
	n = 0
	for i in range(a+1, b):
		if i%c == 0:
			n += 1
	return n

def test(need, res):
	print('[ OK ] '+str(res) if need == res else '[FAIL] '+str(need)+' != '+str(res))

test(0, f(1,2,3))
test(1, f(1,4,3))  # 3
test(0, f(1,3,3))
test(4, f(1,10,2)) # 2,4,6,8
test(8, f(1,10,1)) # 2,3,4,5,6,7,8,9
