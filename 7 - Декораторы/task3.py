#!/bin/env python

'''
3. Каррирование.
  Преобразовать вызов функции с конечным количеством позиционных аргументов f(a, b, c, d)
  в вызов вида f(a)(b)(c)(d), используя декоратор.
  Пример:
  @carry
  def foo(a, b):
        return a + b

   foo(1)(5)  # вернет 6
'''


def carry(handler):
    num_params = handler.__code__.co_argcount
    args = []

    def func(arg):
        args.append(arg)
        if len(args) == num_params:
            return handler(*args)
        return func
    return func


@carry
def foo(a, b):
    return a + b


print(foo(1)(5))  # вернет 6
