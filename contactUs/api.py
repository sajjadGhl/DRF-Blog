from contactUs.models import ContactUs
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ContactUsSerializer
from authentication.permissions import IsAdmin, IsAuthor, IsUser


# Contact Us ViewSet
class ContactUsViewSet(viewsets.ModelViewSet):
    serializer_class = ContactUsSerializer
    queryset = ContactUs.objects.all()

    def create(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            instance = ContactUs.objects.get(pk=pk)
        except ContactUs.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ContactUsSerializer(instance)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = []
        else:
            permission_classes = [IsAdmin | IsAuthor]
        return [permission() for permission in permission_classes]

