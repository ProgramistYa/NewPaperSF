from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
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