#!/bin/env python

'''
4. Написать декоратор, который будет проверять тип аргументов при вызове функции
   согласно аннотации функции. Декорирование функции без аннотации или с неполной
   аннотацией (когда аннотированы не все аргументы) должно рейзить ошибку.
   В случае несовпадения переданных во время вызова функции аргументов с типами
   аргументов в аннотации - выводить сообщение.
'''


def test_anno(handler):
	ann = handler.__annotations__
	for var in handler.__code__.co_varnames:
		if var not in ann:
			raise Exception('No annotation in %s' % handler.__name__)
	ann = list(ann.values())

	def inner(*args, **kvargs):
		for i in range(0, len(ann)):
			if type(args[i]) != ann[i]:
				print("Warning: mismatch type %s, need %s" % (type(args[i]), ann[i]))
		return handler(*args, **kvargs)
	return inner


@test_anno
def func(a: int, b: str):
	print(a, b)


func(1, '2')
func(1, 2)


@test_anno
def func_without_anno(a, b: str):
	print(a, b)
