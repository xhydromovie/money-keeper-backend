from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .api import router
from collection.views import CustomObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth', CustomObtainAuthToken.as_view(), name="authentication"),
]
