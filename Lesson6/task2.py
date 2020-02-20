#!/bin/env python

# Написать генератор списка для получения списка всех публичных атрибутов объекта
class MyObj(object):
	def __init__(self, q):
		self.q = q
	def func1(self):
		pass

obj = MyObj(2)
print([attr for attr in dir(obj)])
