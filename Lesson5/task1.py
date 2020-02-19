#!/bin/env python

from math import sqrt

class Complex(object):
	def __init__(self, a, b=0):
		self.a = a
		self.b = b
	def __eq__(self, y):
		return (abs(self.a - y.a) < 0.01) and (abs(self.b - y.b) < 0.01)
	def __add__(self, y):
		if isinstance(y, Complex):
			dA = y.a
			dB = y.b
		else:
			dA = y
			dB = 0
		return Complex(self.a + dA, self.b + dB)
	def __sub__(self, y):
		if isinstance(y, Complex):
			return self.__add__(Complex(-y.a, -y.b))
		else:
			return self.__add__(Complex(-y))
	# https://ru.wikipedia.org/wiki/Комплексное_число#Умножение
	def __mul__(self, y):
		a = self.a; b = self.b
		c = y.a; d = y.b
		return Complex(a*c-b*d, b*c+a*d)
	# https://ru.wikipedia.org/wiki/Комплексное_число#Деление
	def __truediv__(self, y):
		a = self.a; b = self.b
		c = y.a; d = y.b
		return Complex((a*c+b*d)/(c*c+d*d), (b*c-a*d)/(c*c+d*d))
	def mod(self):
		return sqrt(self.a**2+self.b**2)
	def __getattr__(self, key):
		return self.kwargs[key]
	def __str__(self):
		return '%.2f%s%.2f*i' % (self.a, ('+' if self.b>=0 else ''), self.b)

x = Complex(2, 1)
y = Complex(5, 6)

def mod(x):
	return x.mod()

def test(need, res):
	print('[ OK ] '+str(res) if need == res else '[FAIL] '+str(need)+' != '+str(res))

test( Complex( 3,  1), x+1)
test( Complex( 7,  7), x+y)
test( Complex(-3, -5), x-y)
test( Complex( 4, 17), x*y)
test( Complex(0.26, -0.11), x/y)
test( 2.24, round(mod(x), 2))
test( 7.81, round(mod(y), 2))
