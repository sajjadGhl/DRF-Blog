from .api import CommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/comments', CommentViewSet, 'comments')

urlpatterns = router.urls
