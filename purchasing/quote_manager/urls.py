from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.quote, name='quote'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),


]
