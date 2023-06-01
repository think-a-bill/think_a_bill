from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:product_pk>/', views.detail, name='detail'),
    path('<int:product_pk>/delete/', views.delete, name='delete'),
    path('<int:product_pk>/update/', views.update, name='update'),
    path('<int:product_pk>/likes/', views.likes, name='likes'),
    path('list/', views.product_list, name='product_list'),
]
