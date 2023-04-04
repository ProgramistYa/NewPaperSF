from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view()),

    path('search/', SearchList.as_view(), name='search'),

    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostEdit.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

    path('articles/create/', PostCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/update/', PostEdit.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),

    path('categories/<int:pk>', CategoryListView.as_view(), name='categories_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    #path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
]

