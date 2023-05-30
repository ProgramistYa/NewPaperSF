from .models import *
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = ['id', 'name', ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Category
       fields = ['id', 'grade', ]

