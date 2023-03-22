from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')),
    #path('articles/', include('main.urls_article')),
    #урл для приложений для аутентификации
    path('', include('protect.urls')),
    path('sign/', include('sign.urls'))

]