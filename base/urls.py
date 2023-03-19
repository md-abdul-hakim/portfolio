from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('message/', views.message, name='message'),
    path('location/', views.location, name='location'),
    path('blog/<int:id>/', views.blog, name='blog'),
]
