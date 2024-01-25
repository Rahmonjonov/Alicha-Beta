from django.urls import path
from .views import *

urlpatterns = [
    path('product/', products_list),
    path('product-detail/<int:pk>/', products_detail),
    path('product-add/', products_add),
    path('product-change/<int:pk>/', products_change),
    path('product-delete/<int:pk>/', products_delete),
    path('product-category-filter/', product_filter_category),
    path('product-filter-barcodes-filter/', product_filter_barcodes),
]
