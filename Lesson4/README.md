# Материалы урока

Презентация: https://drive.google.com/open?id=1jn9bMjzM45xm8Mjiyq3FZHgrqH-y4T-O

Общая папка: https://drive.google.com/drive/u/0/folders/1YPUYl44SVeYivPFuE-5L7RNuiWFFeW4h

# Модули и пакеты

```python
import my_module
from my_module import my_function as my_fnc
from my_package.my_module import my_function
from .my_module import my_function # импорт внутри пакета
```

Установка пакета из глобального репозитория `pip install my_package`

Чтобы создать пакет нужно в директорию добавить `__init__.py`,
для сохранения всех зависимостей: `pip freeze > requirements.txt`
