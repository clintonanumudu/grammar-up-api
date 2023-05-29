from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('translate.urls')),
    path('', include('sentence.urls')),
    path('admin/', admin.site.urls),
]