from rest_framework import viewsets
from categories.models import Category
from categories.serializers import CategorySerializer
from authentication.permissions import IsAdmin, IsAuthor
from blog.pagination import CustomPagination
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin | IsAuthor]
    pagination_class = CustomPagination

    def list(self, request):
        search = self.request.query_params.get('search')

        if search is not None:
            self.queryset = self.filter_queryset(self.queryset.filter(title__icontains=search))

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAdmin | IsAuthor]
        return [permission() for permission in permission_classes]
