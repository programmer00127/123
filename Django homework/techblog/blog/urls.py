from django.urls import path
from . import views


# Простір імен для додатку, щоб уникнути конфліктів з іншими додатками
app_name = 'blog'


urlpatterns = [
    # Головна сторінка блогу
    path('', views.home_view, name='home'),


    # Сторінка перевірки досвіду користувача
    path('experience/', views.check_experience, name='experience'),


    # Сторінка популярних постів
    path('popular/', views.popular_posts, name='popular'),
]

