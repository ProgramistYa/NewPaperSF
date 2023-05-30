from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # подключаем встроенные эндопинты для работы с локализацией
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')),
    #path('articles/', include('main.urls_article')),
    #урл для приложений для аутентификации
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
]