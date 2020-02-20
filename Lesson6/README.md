# Материалы урока

Итераторы: https://drive.google.com/open?id=144Efv_-EpAPe45Xdr43EKnnFjsaW0Gau
Генераторы: https://drive.google.com/open?id=1d0CdsakUkDTIcJwUR0thNAsPpHkgh3Af

Общая папка: https://drive.google.com/drive/u/0/folders/1_D2IjVxYkYHcFRSRuRwXrlwT6jc1cr63

# Исключения
```python
try:
	raise Exception()
except Exception:
	pass
else: # если не было исключений
	pass
finally:
	pass
```

# Итераторы
```python
class SimpleIterator(object)
	def __init__(self, max=1):
		self.max = max
		self.ck = 0
	def __iter__(self):
		return self
	def __next__(self):
		if self.ck < self.max:
			self.ck += 1
			return 1
		else:
			raise StopIteration()

for i in SimpleIteration(5)
	print(i)
```

# Генераторы
```python
# генератор списка
for i in [i+20 for i in range(5)]
	print(i)

# убираем элемент из массива
a = [1,2,3,4]
b = [i for i in a if i != 2]

# работа со словарём
a = {'a':1,'b':2}
b = {v:k for k,v in a.items()} # 1:'a', 2:'b'

# функция-генератор
def gen_sq(n):
	for i in range(n):
		yield i**2

for i in gen_sq(5):
	print(i)

gen = gen_sq(5) # <generator>
next(gen) # 0
next(gen) # 1
next(gen) # 4

# выражение генератор <generator>
(x**2 for x in range(3))
```
