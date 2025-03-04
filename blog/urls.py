from django.urls import path
from .views import news_view  # Импортируем только news_view

urlpatterns = [
    path("news/", news_view, name="news_list"),  # Главная страница теперь показывает новости
]

