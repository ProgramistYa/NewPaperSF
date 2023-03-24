from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, Group

from allauth.account.forms import SignupForm
#форма, которая будет заполняться пользователем
class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    firts_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = ("username",
                  "firts_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",
                  )

# форму регистрации SignupForm, которую предоставляет пакет allauth.
class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user