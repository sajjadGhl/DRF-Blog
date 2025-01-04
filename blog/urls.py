from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

'''
POSTS:
    schedule                ✔
    limit to 10             ✔
    filter base category    

Post Page:
    Show their category     ✔
        
CATEGORY:
    for posts               ✔
    search                  ✔
    list                    ✔
    create                  ✔
    edit                    ✔
    delete                  ✔
    get                     ✔
        
COMMENT:
    Dont have Update        ✔
    Show post comment only to Admin, own Author ✔

Home Page:
    Show each category last posts
    Important category at first
    
pages should be Responsive

'''

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('accounts.urls')),
    path('', include('contactUs.urls')),
    path('', include('categories.urls')),
    path('', include('comments.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
