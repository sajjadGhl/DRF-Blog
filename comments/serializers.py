from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'post')

    def to_representation(self, instance):
        rep = super(CommentSerializer, self).to_representation(instance)
        rep['user'] = instance.user.first_name
        return rep
