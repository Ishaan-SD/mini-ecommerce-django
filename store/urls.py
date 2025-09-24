from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name = 'product_list'),
    # path('order/<int:order_id>/add-item/', views.add_to_cart, name = "add_to_cart"),
    path('product/<int:pk>/', views.product_detail, name='product_detail')
]