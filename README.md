# Yamdb

![yamdb](https://github.com/CapitainFan/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Настройка CI/CD процессов для проекта, который собирает отзывы для пользователей на различные произведения.

## Технологии :
- ООП
- DRF
- Django
- Docker
- Git
- GitHub Actions
- Gunicorn
- Nginx
- REST API
- PostgreSQL
- Python 3.7
- pytest
- flake8

## Ссылка на мой проект :

http://notify.ddns.net/api/v1/

## Как использовать проект

### Установка Docker с инструкциями с официального сайта :

- для [Windows и MacOS](https://www.docker.com/products/docker-desktop) 
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Установите [Docker Compose](https://docs.docker.com/compose/install/)


### Установка проекта (Linux Ubuntu)

- Создайте папку для проекта YaMDb `mkdir yamdb` и перейдите в нее `cd yamdb`
- Склонируйте этот репозиторий в текущую папку `git clone git@github.com:CapitainFan/yamdb_final.git`
- Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения для работы с базой данных:

```
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнер в котором будет развернута БД)
DB_PORT=5432 # порт для подключения к БД
```

- Запустите docker-compose `sudo docker-compose up -d` 
- Примените миграции `sudo docker-compose exec web python manage.py migrate`
- Соберите статику `sudo docker-compose exec web python manage.py collectstatic --no-input`
- Создайте суперпользователя Django `sudo docker-compose exec web python manage.py createsuperuser --email 'admin@yamdb.com'`


## Примеры эндпоинтов

- Создать пользователя        /api/v1/auth/signup/

```
{ "email": "string", "username": "string" }
```
- Получить Jwt Token      /api/v1/auth/token/
```
{ "username": "string", "confirmation_code": "string" }
```

- Категории      /api/v1/categories/
- Жанры         /api/v1/genres/
- Произведения         /api/v1/titles/
- Отзывы        /api/v1/titles/1/reviews/
- Комментарии       /api/v1/titles/1/reviews/1/comments/
- Пользователи          /api/v1/users/


## Автор

Богдан Сокольников
