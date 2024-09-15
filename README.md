# mvp_project_1
Тестовое задание: подключение к mongo db, создание пользователя

## Dependency Installation
Скачивание репозитория:
'''
git clone git@github.com:confuoko/mvp_project_1.git
'''

Создание и активация виртуального окружения:
'''
python -m venv venv
'''
'''
source venv/Scripts/activate
'''
'''
pip install -r requirements.txt
'''

Выполнить миграции:
'''
python manage.py migrate
'''

Создадим суперпользователя через терминал командой:
'''
python manage.py createsuperuser
'''
(username: admin
email adress: admin@mail.ru
password: 12345)

Запустим наш сервер командой: '''python manage.py runserver''',
переходим в админку по ссылке: http://127.0.0.1:8000/admin/ и логинимся от имени суперпользователя.

Создадим еще парочку пользователей через админку. Данные о пользователях сохраняются в базе данных 
mongodatabase в коллекции auth_user. 

## Eddpoint
Для получения информации из данной коллекции через get-запрос postman в проекте доступен 
эндпоинт: http://127.0.0.1:8000/users/.
Ответ возвращается в формате json.





