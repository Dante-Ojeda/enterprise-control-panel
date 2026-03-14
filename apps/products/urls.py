from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_inventory, name='inventory'),
    path('price-list/', views.product_price_list, name='price-list' ),
    path('detail/', views.product_detail, name='detail' ),
    path('comparator/', views.product_comparator, name='comparator' )
]