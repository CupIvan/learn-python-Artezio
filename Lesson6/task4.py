#!/bin/env python

# Написать функцию-генератор cycle которая бы возвращала циклический итератор.
def cycle(a):
	i = 0; max = len(a)
	while True:
		if i == max: i = 0
		yield a[i]
		i += 1


doit = 10
for i in cycle([1,2,3]):
	if not doit: break
	doit -= 1
	print(i)
