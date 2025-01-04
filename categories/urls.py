from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import CategoryViewSet

router = DefaultRouter()
router.register(r'api/categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
