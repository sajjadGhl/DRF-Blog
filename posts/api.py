from posts.models import Post
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import PostSerializer
from authentication.permissions import IsAdmin, IsAuthor, IsUser, IsOwner
from blog.pagination import CustomPagination
from django.utils import timezone
from django.db.models import Q


# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    queryset = Post.objects.exclude(created_at__gt=timezone.now())
    # queryset = Post.objects.all()

    pagination_class = CustomPagination

    def list(self, request):
        search = self.request.query_params.get('search')

        if search is not None:
            self.queryset = self.filter_queryset(
                self.queryset.filter(Q(title__icontains=search) | Q(content__icontains=search))
            )

        page = self.paginate_queryset(self.queryset)

        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        request.data['author'] = request.user.id
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = Post.objects.get(pk=pk, created_at__lte=timezone.now())
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            instance = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, instance)

        serializer = PostSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            instance = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, instance)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAdmin | (IsAuthor & IsOwner)]
        return [permission() for permission in permission_classes]
