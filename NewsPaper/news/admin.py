from django.contrib import admin
from .models import *

from modeltranslation.admin import TranslationAdmin


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ['author', 'content', 'time_in', 'title',
                    'content_rate']  # генерируем список имён всех полей для более красивого отображения
    list_filter = ('author', 'category')  # добавляем примитивные фильтры в нашу админку
    # search_fields = ('')   #   тут всё очень похоже на фильтры из запросов в базу


# class TranslatedPostAdmin(TranslationAdmin):
#     model = Post
#
# class CategoryAdmin(TranslationAdmin):
#     model = Category


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)
# admin.site.register(AddNewInProject)
