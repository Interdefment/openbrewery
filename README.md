## Quickstart

Инициализация виртуального окружения

`python -m venv venv`

Активация виртуального окружения (windows)

`./venv/Scripts/activate`

Установка зависимостей

`pip install -r requirements.txt`

Создание миграций

`python manage.py makemigrations`

Применение миграций

`python manage.py migrate` 

Запуск сервера -> localhost:8000

`python manage.py runserver 8000`

## Для загрузки данных необходимо выполнить переход в браузере на следующие страницы:

**Пересоздать (или создать с нуля) основные brewery types, указанные на https://www.openbrewerydb.org/documentation/01-listbreweries**

`localhost:8000/create_types`

Не является обязательным для загрузки данных

**Загрузить данные с https://api.openbrewerydb.org**

`localhost:8000/download_data`

*Query параметры* (`localhost:8000/download_data?parameter1=value1&parameter2=value2`)

`clear_all=true` Очистить все записи в таблице breweries

Следующие поддерживаемые параметры описаны на https://www.openbrewerydb.org/documentation/01-listbreweries

`per_page=<int>`

`page=<int>`

`by_type=<string>` 

`by_city=<string>`
