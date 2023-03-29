from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View
)
from django.shortcuts import render, reverse, redirect, get_object_or_404
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Category
from .filters import PostFilter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#для расслыок на почту по емейлу
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from django.db.models.signals import post_save

class PostList(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset

        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreate(PermissionRequiredMixin, CreateView, LoginRequiredMixin):
    form_class = PostForm
    model = Post
    permission_required = 'news.add_post'
    template_name = 'post_create.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 20
        return super().form_valid(form)

class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    permission_required = 'news.delete_post'
    success_url = reverse_lazy('post_list')

class PostEdit(PermissionRequiredMixin, UpdateView, LoginRequiredMixin):
    # для проверки аунтефикации LoginRequiredMixin
    form_class = PostForm
    model = Post
    permission_required = 'news.change_post'
    template_name = 'post_edit.html'

#представление поиска . сделал просто Страницу всех новостей!!!!
class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    #context_object_name - ИМЯ которое будет в html файле!
    context_object_name = 'news'
    ordering = '-time_in'

# CATEGORY EMAIL

#Добавьте пользователю возможность подписываться на рассылку новостей в какой-либо категории
@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)

    if not category.subscribers.filter(id=user.id).exists():
        category.subscribers.add(user)
        email = user.email
        html = render_to_string('subscrib.html',
                                {'category': category,
                                 'user': user
                                 }
                                )
        msg = EmailMultiAlternatives(
            subject=f'{category} subscription',
            body='',
            from_email='s-ya98@yandex.com',
            to=[email])
        msg.attach_alternative(html, "subscrib/html")
        try:
            msg.send()
        except Exception as e:
            print(e)
        return redirect('protect:index')
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)

    if category.subscribers.filter(id=user.id).exists():
        category.subscribers.remove(user)
    return redirect('protect:index')


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

# CATEGORY LIST

class CategoryListView(ListView):
    model = Post
    template_name = 'message_mail.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context