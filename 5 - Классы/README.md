# Материалы урока

Презентация: https://drive.google.com/open?id=1hJkw47Df6RrSfy2UvI9UOGygVBAQHgY8

Общая папка: https://drive.google.com/drive/u/0/folders/1IIYWDYRBwH5uwAmBuRbxlWhwIL8jzNSE

# Классы и ООП

```python
class Clock(object):
	def __init__(self, attr1, attr2=None)
		pass # заглушка
	def __getattr__(self, item) # обращение по точке: casio.attribute1
		pass
	def __add__(self, other) # перегрузка +
		pass
	def __lt__(self, other) # <
		pass
casio = Clock()

class Clock2(Clock): # наследоваться можно также от нескольких через запятую при этом методы сначала ищутся родителях, которые слева
	def my_method(self):
		super(Clock, self).parent_method() # вызов метода у родителя
```
