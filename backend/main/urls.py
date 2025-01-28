from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('action/<int:pk>/', views.ActionView.as_view(), name='action'),
    path('product-list/', views.ProductListView.as_view(), name='product-list'),
    path('admin/', admin.site.urls),
]