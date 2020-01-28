#!/bin/env python
'''
3. Написать функцию, которая будет принимать только 4 позиционных аргумента (все аргументы числовые).
    Функция должна вернуть среднее арифметическое аргументов и самый большой аргумент за все время вызовов этой функции.
    Пример: foo(1,2,3,4) -> 2.5, 4
                  foo(-3, -2, 10, 1) -> 1.5, 10
                  foo(7,8,8,1) -> 6, 10
'''

def foo(*args):
	if not hasattr(foo, 'm'): foo.m = 0
	_m = max(args)
	if foo.m < _m: foo.m = _m
	return (sum(args) / len(args), foo.m)

def test(need, res):
	print('[ OK ] '+str(res) if need == res else '[FAIL] '+str(need)+' != '+str(res))

test( (2.5, 4),  foo(1,2,3,4))
test( (1.5, 10), foo(-3, -2, 10, 1))
test( (6, 10),   foo(7,8,8,1))
