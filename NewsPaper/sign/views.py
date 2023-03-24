from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
    # мб попробовать ?! success_url = '/news/'


# добавьте миксин ограничения прав и в атрибуте класса-представления пропишите,
# какими правами должен обладать пользователь для доступа к этой странице.
# class ProtectedView(LoginRequiredMixin, TemplateView):
#     template_name = 'index.html'


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')