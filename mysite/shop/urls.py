from .views import *
from django.urls import path

urlpatterns = [
    path('customuser/', CustomUserViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='customuser_list'),
    path('customuser/<int:pk>/', CustomUserViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='customuser_detail'),

    path('category/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('product/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='product_list'),
    path('product/<int:pk>/', ProductViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),

    path('order/', OrderViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='order_list'),
    path('order/<int:pk>/', OrderViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='order_detail'),

    path('orderitem/', OrderItemViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='orderitem_list'),
    path('orderitem/<int:pk>/', OrderItemViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='orderitem_detail'),

    path('payment/', PaymentViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='payment_list'),
    path('payment/<int:pk>/', PaymentViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='payment_detail'),
]