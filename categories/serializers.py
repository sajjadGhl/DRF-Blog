from rest_framework import serializers
from .models import Category
from posts.serializers import PostSerializer


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'posts')
