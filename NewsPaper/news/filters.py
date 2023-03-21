import django_filters
from .models import Post
from django_filters import DateFilter, CharFilter, FilterSet
from django import forms


# можно выполнить фильтрацию сразу по нескольким критериям
#пока так но с фалед_найм могу ошибиться!
class PostFilter(FilterSet):
    date_time__gt = DateFilter(field_name='data_time',
                               widget=forms.DateInput(attrs={'type': 'date'}),
                               lookup_expr='gt',
                               label='Опубликовано после')

    # author_relation = CharFilter(field_name='author__user__username',
    #                              lookup_expr='icontains',
    #                              label='Автор')
    # post_title = CharFilter(field_name='title',
    #                         lookup_expr='icontains',
    #                         label='Post название')

    class Meta:
        model = Post
        fields = ['title', 'author']