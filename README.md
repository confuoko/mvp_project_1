# mvp_project_1
Тестовое задание:
-   создать сервер на Django/Flask (для Python)
-   подключить базу данных (mongo DB),
-   создать пользователя в базе данных,
-   проверить как работает, через Postman

## Dependency Installation

Скачивание репозитория:
`git clone git@github.com:confuoko/mvp_project_1.git`
  
Создание и активация виртуального окружения:
```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
## В случаe, если Вы работаете с новой базой данных:
Выполните миграции (для работы с Вашей базой данных):
`python manage.py migrate`

Создайте суперпользователя через терминал командой:
`python manage.py createsuperuser`
```
username:		admin,
email adress:	admin@mail.ru
password:		12345
```
Запустим наш сервер командой:
`python manage.py runserver`

Переходим в админку по ссылке: http://127.0.0.1:8000/admin/ и логинимся от имени суперпользователя.

Создадим еще парочку пользователей через админку. Данные о пользователях сохраняются в базе данных `mongodatabase` в коллекции `auth_user`.

## Endpoint

Для получения информации из данной коллекции через get-запрос postman в проекте доступен эндпоинт: http://127.0.0.1:8000/users/. Ответ возвращается в формате json.