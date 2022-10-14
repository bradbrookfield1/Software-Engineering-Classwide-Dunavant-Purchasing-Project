from django.urls import path
from .views import (
    AssetListView,
    AssetDetailView,
    AssetCreateView,
    AssetUpdateView,
    AssetDeleteView,
    LogListView,
    LogDeleteView
)

app_name = 'inventory'
urlpatterns = [
    path('', AssetListView.as_view(), name='asset-list'),
    path('asset/<int:pk>/', AssetDetailView.as_view(), name='asset-detail'),
    path('new/', AssetCreateView.as_view(), name='asset-create'),
    path('asset/<int:pk>/update/', AssetUpdateView.as_view(), name='asset-update'),
    path('asset/<int:pk>/delete/',
         AssetDeleteView.as_view(), name='confirm-delete'),
    path('logs/', LogListView.as_view(), name='log-list'),
    path('logs/<int:pk>/delete/',
         LogDeleteView.as_view(), name='log-confirm-delete'),
]
