# Тест сайта saucedemo.com


e2e тест для проверки сценария покупки товара на сайте saucedemo.com с использованием Python + Selenium.
Тест проверяет процесс от авторизации до завершения покупки.

[Python3](https://www.python.org/downloads/) должен быть уже установлен.

Cоздаём виртуальное окружение
```python
python -m venv venv
```
Путь до корневой папки 
```python 
venv/scripts/activate
```

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```python
pip install -r requirements.txt
```

## Как работает
    
- ### Для запуска теста:
    ```python
  pytest
  ```
  
 ## Если нужен отчет

- ### Для создания `allure` отчета:
  Запустить следующую команду
    ```python
    pytest --alluredir=results
    ```
- ### Для просмотра `allure` отчета:
  Запустить следующую команду

    ```python
    allure serve results
    ```
