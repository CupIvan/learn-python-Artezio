#!/bin/env python

# Напишите итератор EvenIterator, который позволяет получить из списка все элементы, стоящие на чётных индексах.

class EvenIterator(object):
	def __init__(self, a):
		self.a = a
		self.ck = 1
	def __iter__(self):
		return self
	def __next__(self):
		if self.ck >= len(self.a):
			raise StopIteration()
		self.ck += 2
		return self.a[self.ck - 2]

for i in EvenIterator([1,2,3,4,5,6,7]):
	print(i)
