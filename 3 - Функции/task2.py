#!/bin/env python
'''
2. Написать функцию, которая принимает произвольное количество любых аргументов.
    Аргументами могут быть вложенные списки и кортежи, содержащие числа и другие списки и кортежи.
    Пример вызова функции: foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
    Функция должна вернуть произведение и сумму всех ненулевых элементов вложенных чисел.
    Возможны циклические ссылки в аргументах. Пример такого аргумента: a = [1, 2, 3]; a.append(a)
    При обнаружении циклической ссылки нужно сообщить пользователю и вернуть None.
'''

def has_cycle(a) -> bool:
	for i in range(len(a)):
		if a[i] == a:
			return True
		if isinstance(a[i], (list)) and has_cycle(a[i]):
			return True
	return False

def f(*args, **kwargs):
	s = 0; m = 1

	for i in range(len(args)):
		if isinstance(args[i], (list, tuple)):
			if has_cycle(args[i]): return None
			for j in range(len(args[i])):
				res = f(args[i][j])
				m *= res[0]
				s += res[1]
			continue
		if args[i] != 0:
			m *= args[i]
			s += args[i]
	for k in kwargs:
		if isinstance(kwargs[k], (list, tuple)) and has_cycle(kwargs[k]): return None
		res = f(kwargs[k])
		m *= res[0]
		s += res[1]
	return m, s

def test(need, res):
	print('[ OK ] '+str(res) if need == res else '[FAIL] '+str(need)+' != '+str(res))

test((8,7), f(1,2,4))
test((8,6), f(0,2,4))
test((8,6), f(0,2,[4]))
test((8,6), f(0,(2),4))
test((24,9), f(0,a=(2,3),c=4))
test((1596672000,75), f(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []])))

a = [1, 2, 3]; a.append(a)
test(None, f(a))
b = [2, 3]; b.append(a)
test(None, f(b))
test(None, f(x=b))
