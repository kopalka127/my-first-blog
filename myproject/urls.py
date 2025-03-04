from django.contrib import admin
from django.urls import path, include
from blog.views import news_view  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", news_view, name="home"),  
    path("news/", news_view, name="news_list"),
]




#path("", post_list, name="home"),

