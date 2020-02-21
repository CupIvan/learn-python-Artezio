#!/bin/env python
'''
3. Написать функцию вычисления факториала числа
'''

def faq(x):
	if x <= 1: return 1
	n = 1
	for i in range(1, x+1): n *= i
	return n

def test(need, res):
	print('[ OK ] '+str(res) if need == res else '[FAIL] '+str(need)+' != '+str(res))

test( 1, faq(0))
test( 1, faq(1))
test( 2, faq(2))
test( 6, faq(3))
test(24, faq(4))
