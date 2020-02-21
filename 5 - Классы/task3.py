#!/bin/env python

class Observable(object):
	def __init__(self, **kwargs):
		self.kwargs = kwargs
	def __str__(self):
		return self.__class__.__name__+'('+self.kwargs.__str__()+')'
	def __getattr__(self, key):
		return self.kwargs[key]

class X(Observable):
	pass
x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print(x)
print(x.foo)
print(x.name)
print(x._bazz)
