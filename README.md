## Документация
#### Установка и запуск на локальном сервере:
1. Клонировать или сохранить репозиторий
1. Создать и активировать виртуальное окружение
   ```
    python3.9 -m venv env 
    . ./env/bin/activate
   ```
2. Установить необходимые пакеты 

   ```
   pip install -r requirements.txt
   ```
3. Запуск локального сервера (предварительно настроив БД в **settings.py** (**"main"** для удалённой БД, **"local_testing_db"** для запуска тестов))
   ```
   cd ./eco_products/
   python3.9 manage.py runserver
___

#### Api-endpoints для работы с БД
- Получить все категории товаров и массив ассоциативных с ними товаров (**GET**):
    -  ``domain.ru/api/category``
- Получить массив всех товаров (**GET**):
    - ``domain.ru/api/products``
- Получить категорию по слагу и массив ассоциативных с ней товаров (**GET**):
    - ``domain.ru/api/category/[slug]``
- Получить продукт по слагу (**GET**):
    - ``domain.ru/api/product/[slug]``
- Получить массив продуктов по слагу категории (**GET**):
    - > ``domain.ru/api/category-product/[category_slug]``  
- Добавить категорию (**POST (form-data or JSON)**):
    - ``` **domain.ru/api/category```
        > {</br>
            **"name"**: "Масло",</br>
            **"slug"**: "butter"</br>
            }
- Добавить продукт (**POST (form-data or JSON)**):
    - ``domain.ru/api/products``
        > {</br>
            **"name"**: "Мёд",</br>
            **"category"**: "honey",</br>
            **"slug"**: "honey3",</br>
            **"description"**: "some_text_here",</br>
            **"qty"**: 500,</br>
            **"price"**: 5000,</br>
            }           

