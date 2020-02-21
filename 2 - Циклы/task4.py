#!/bin/env python
'''
4. Написать свою имплементацию функции range() из Python 2.x (аналогично Python 3, только возвращает список).
'''

def range2(start, stop=None, step=None):
	if stop is None: # передали только один параметр
		stop = start
		start = 0
	if step is None:
		step = 1
	res = []
	if step == 0: return res
	i = start
	while i >= start and i < stop:
		res.append(i)
		i += step
	return res

def test(need, res):
	print('[ OK ] '+str(res) if need == res else '[FAIL] '+str(need)+' != '+str(res))

test([],    range2(0))
test([0],   range2(1))
test([0,1], range2(2))
test([],    range2(0,0))
test([1],   range2(1,2))
test([1,2], range2(1,3))
test([],    range2(1,3,0))
test([1],   range2(1,3,2))
test([1,3], range2(1,4,2))
test([1],   range2(1,4,-1))
test([-1,0],range2(-1,1))

