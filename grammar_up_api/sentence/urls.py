from django.urls import path
from . import views

urlpatterns = [
    path('sentence/', views.sentence, name='sentence'),
]
