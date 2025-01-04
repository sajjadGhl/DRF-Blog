from rest_framework import serializers
from .models import Post
from comments.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    image = serializers.FileField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'author', 'created_at', 'categories', 'comments')

    def to_representation(self, instance):
        rep = super(PostSerializer, self).to_representation(instance)
        rep['author'] = instance.author.first_name
        rep['categories'] = [category.title for category in instance.categories.all()]
        # rep['comments'] = [comment.title for comment in instance.comments.all()]
        return rep
