from django import forms
from django.core.exceptions import ValidationError
from .models import Post

from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm

class PostForm(forms.ModelForm):
    content_text = forms.CharField(min_length=20)

    class Meta:
        content = 'NW'
        model = Post
        fields = [
            'author',
            'title',
            'category',
            'content',
            'content_rate',
            'content_text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        content_text = cleaned_data.get('content_text')

        if title is None:
            raise ValidationError({
                'title': 'Укажите понятный заголовок.'
            })
        if content_text == title:
            raise ValidationError({
                'content_text': 'Заголовок совпадает с текстом'
            })
        if title == content:
            raise ValidationError({
                "Заголовок не должен быть идентичным контенту."
            })
        if len(content_text) < 15:
            raise ValidationError({
                'content_text': 'Пишите более подробный текст.'
            })

        return cleaned_data

class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user