#!/bin/env python

'''
1.Напишите параметризованный декоратор, который считает и выводит при
  каждом вызове среднее время работы функции за n последних вызовов.
  Время выводить в миллисекундах.
  Пример использования:
  @average_time(n=2)
  def foo(a):
    sleep(a)
    return a

  foo(3) # вернет 3 и выведет сообщение "Среднее время работы: 3000 мс."
  foo(7) # вернет 7 и выведет сообщение "Среднее время работы: 5000 мс."
  foo(1) # вернет 1 и выведет сообщение "Среднее время работы: 4000 мс."
'''

from time import sleep, time
from functools import wraps


def average_time(n=1):
    def inner(handler):
        a = []
        @wraps(handler)
        def wrapper(*args, **kvargs):
            t = time()
            res = handler(*args, **kvargs)
            dt = time() - t
            a.append(dt)
            if len(a) > n:
                a.pop(0)
            print('Среднее время работы: %d мс.' % round(sum(a) / len(a) * 1000))
            return res
        return wrapper
    return inner


@average_time(n=2)
def foo(a):
    sleep(a)
    return a


print(foo(3))  # вернет 3 и выведет сообщение "Среднее время работы: 3000 мс."
print(foo(7))  # вернет 7 и выведет сообщение "Среднее время работы: 5000 мс."
print(foo(1))  # вернет 1 и выведет сообщение "Среднее время работы: 4000 мс."
