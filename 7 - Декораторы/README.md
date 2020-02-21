# Материалы урока

Итераторы: https://drive.google.com/open?id=144Efv_-EpAPe45Xdr43EKnnFjsaW0Gau
Генераторы: https://drive.google.com/open?id=1d0CdsakUkDTIcJwUR0thNAsPpHkgh3Af

Общая папка: https://drive.google.com/drive/u/0/folders/1_D2IjVxYkYHcFRSRuRwXrlwT6jc1cr63

# Декораторы
```python
@decorator
def foo(x, y): pass
foo = decorator(foo) # тоже самое

@decorator_with_params(param=5)
def foo(x, y): pass
foo = decorator_with_params(param=5)(foo) # тоже самое

# множественные декораторы
@decorator
@decorator_with_params(param=5)
def foo(x, y): pass
```

# Простой декоратор
```python
from functools import wraps

def my_decor(handler):
	@wraps(handler) # нужно чтобы правильно выставились атрибуты декорируемой функции (например, __name__)
	def wrapper(*args, **kwargs):
		return handler(*args, **kwargs)
	return wrapper

@my_decor
def foo(a):
	print("A")
	return a
```

# Параметризированный декторатор
```python
from functools import wraps

def my_decor(p=4):
	def my_decor_inner(handler):
		@wraps(handler)
		def wrapper(*args, **kwargs):
			return handler(*args, **kwargs)
		return wrapper
	return my_decor_inner

@my_decor(p=1)
def foo(a):
	print("A")
	return a
```

# Популярные декораторы
```python
class Spam:
	b = 1
	def __init__(self, b):
		self.b = b

	@classmethod
	def print_b(cls):
		print(cls.b)

	@staticmethod
	def print_msg(st)
		print(st)

	@property
	def my_param(self):
		return self.b * 3

a = Spam(12)
assert a.b == 12
a.print_b()    # 1
Spam.print_b() # 1
a.print_msg('abc')
Spam.print_msg('abc')
a.print_msg('abc')
assert a.my_param == 36
```
