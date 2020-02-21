#!/bin/env python

'''
2. Напишите параметризованный декоратор для классов,
   который будет считать и выводить время работы методов класса,
   имена которых переданы в параметрах декоратора.
Пример:
  @time_methods('inspect', 'finalize')
  class Spam:
      def __init__(self, s):
          self.s = s
      def inspect(self):
           sleep(self.s)
      def foo(self):
           return self.s

 a = Spam(2)
 a.inspect()  #  должно вывести сообщение о времени работы
 a.foo()  # ничего не выводить
'''


from time import sleep, time


def time_methods(*methods):
    def inner(cls):
        class wrapper(object):
            def __init__(self, *args, **kvargs):
                cls.__init__(cls, *args, **kvargs)

            def __getattr__(self, method):
                def handler(*args, **kvargs):
                    t = time()
                    attr = getattr(cls, method)
                    res = attr(cls, *args, **kvargs)
                    if method in methods:
                        print('Среднее время работы: %d мс.' % round((time() - t) * 1000))
                    return res
                return handler
        return wrapper
    return inner


@time_methods('inspect', 'finalize')
class Spam:
    def __init__(self, s):
        self.s = s

    def inspect(self):
        sleep(self.s)

    def foo(self):
        return self.s


a = Spam(1)
a.inspect()  # должно вывести сообщение о времени работы
a.foo()  # ничего не выводить
