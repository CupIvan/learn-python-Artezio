#!/bin/env python

# Написать функцию-генератор chain, которая последовательно итерирует переданные объекты (произвольное количество)
def chain(*args):
	for obj in args:
		yield obj

for i in chain(1,2,['d'],{'a':3},'fff'):
	print(i)
