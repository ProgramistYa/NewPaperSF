from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)
#admin.site.register(AddNewInProject)

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('data_time', 'post_title', 'post_text', 'post_rating')
# admin.site.register(Post, PostAdmin)



