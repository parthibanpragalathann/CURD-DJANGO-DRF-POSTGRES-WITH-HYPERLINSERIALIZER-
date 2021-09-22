# Django, DRF with Postgresql using Hyperlink Serializer Model of CURD operations in multiple model  

## Concepts of DRONE applications 

## Create Database

## Create and activate virtual environment

## Installed Packages or Dependencies 

````python 
pip install django, django-filter, django-rest-knox, djangorestframework, psycopg2
````

## Create django project and app

````python 
django-admin startproject drone_api

django-admin startapp drone_app
````
## Application definition(settings.py)

````python 
INSTALLED_APPS = [
    'drone_app',
    'rest_framework',
]
````
## DB Connections (settings.py)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DRONE',
        'USER': 'postgres',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Applications urls

````python API URLS - 
     
     http://127.0.0.1:8000/api/
    "drone/category": "http://127.0.0.1:8000/api/drone/category/",
    "drone": "http://127.0.0.1:8000/api/drone/",
    "pilot": "http://127.0.0.1:8000/api/pilot/",
    "competitions": "http://127.0.0.1:8000/api/competitions/"
````




