# Материалы урока

Презентация: https://drive.google.com/open?id=1EPp0lKedcFwAyebNAQc9VRXeXuNgMcUB

Общая папка: https://drive.google.com/drive/u/0/folders/1SEUuxeZSmbhw_RpEPszByyPO4dV06V7d

# Функции

```python
def func1(arg1, arg2=2):
    v1 = arg1
    v2 = arg2
    return v1, v2

def func2(*args): # func2(1,2,3,4)
def func2(**kwargs): # func2(a=1,b=2)
def func3(*, a, b=True): # func3(a=1)

sum = lambda a,b=4: a+b

def foo(a:int, b:'desc'=3, *, c:tuple) -> dict:
```
