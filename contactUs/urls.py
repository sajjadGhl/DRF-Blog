from django.urls import path, include
from .api import ContactUsViewSet
from rest_framework.urlpatterns import format_suffix_patterns

contactUs_list = ContactUsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

contactUs_detail = ContactUsViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = format_suffix_patterns([
    path('api/contactUs', contactUs_list, name='contactUs-list'),
    path('api/contactUs/<int:pk>/', contactUs_detail, name='contactUs-detail'),
])
