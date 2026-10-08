TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',


        # Додаткові шляхи до шаблонів (глобальна папка templates у проєкті)
        'DIRS': [BASE_DIR / 'templates'],


        # Шукати шаблони також у кожному додатку (папка app_name/templates/)
        'APP_DIRS': True,


        'OPTIONS': {
            'context_processors': [
                # Додає інформацію для налагодження
                'django.template.context_processors.debug',


                # Додає об’єкт request у шаблони
                'django.template.context_processors.request',


                # Додає користувача (user) та систему аутентифікації
                'django.contrib.auth.context_processors.auth',


                # Додає повідомлення (messages) у шаблони
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = [
    # Стандартні додатки Django
    'django.contrib.admin',          # Адмін-панель
    'django.contrib.auth',           # Система аутентифікації
    'django.contrib.contenttypes',   # Типи контенту (зв’язки моделей)
    'django.contrib.sessions',       # Сесії користувачів
    'django.contrib.messages',       # Повідомлення (flash messages)
    'django.contrib.staticfiles',    # Робота зі статичними файлами (CSS, JS)


    # Наші власні додатки
    'blog',  # приклад кастомного додатку
]


import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ... інші налаштування ...# Налаштування статичних файлів*
STATIC_URL = '/static/'  # URL префікс для статичних файлів# Папки, де Django шукає статичні файли під час розробки*
STATICFILES_DIRS = [
    BASE_DIR / 'static_files',  # Глобальні статичні файли для TechBlog*
]

# Папка, куди збираються всі статичні файли для production*
STATIC_ROOT = BASE_DIR / 'collected_static'

# Для розробки*
DEBUG = True  # Поки що залишаємо True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
