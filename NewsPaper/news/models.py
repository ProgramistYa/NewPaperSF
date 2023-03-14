from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User



class Author(models.Model):
    user_relation = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)

    def update_rating(self):
        articles = Post.objects.filter(author=self)
        articles_rating = articles.aggregate(Sum('content_rate')).get('content_rate__sum')
        comments = Comment.objects.filter(comment_user=self.user_relation)
        comments_rating = comments.aggregate(Sum('comment_rate')).get('comment_rate__sum')
        comments_to_author = Comment.objects.filter(post_id=self.id)
        to_author_rating = comments_to_author.aggregate(Sum('comment_rate'))['comment_rate__sum']
        total_rating = articles_rating * 3 + comments_rating + to_author_rating
        self.rating = total_rating
        self.save()


class Category(models.Model):
    subject = models.CharField(max_length=100, unique=True)

news = 'NW'
article = 'AC'
CONTENTS = [
    (news, 'Новость'),
    (article, 'Статья')
]


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=10, choices=CONTENTS)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    content_text = models.TextField()
    content_rate = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.title} - {self.content_text}'

    def like(self):
        self.content_rate += 1
        self.save()
        #return self.content_rate

    def dislike(self):
        self.content_rate -= 1
        self.save()
        #return self.content_rate

    def preview(self):
        return f'{self.content_text[:124]}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    comment_rate = models.IntegerField(default=1)

    def like(self):
        self.comment_rate += 1
        self.save()
        #return self.comment_rate

    def dislike(self):
        self.comment_rate -= 1
        self.save()
        #return self.comment_rate
