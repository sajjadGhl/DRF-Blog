from comments.models import Comment
from comments.serializers import CommentSerializer
from authentication.permissions import IsAdmin, IsAuthor, IsOwner
from blog.pagination import CustomPagination
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'post', 'delete']

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'delete':
            permission_classes = [IsAdmin | (IsAuthor & IsOwner)]
        return [permission() for permission in permission_classes]
