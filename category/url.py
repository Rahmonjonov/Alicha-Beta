from django.urls import path
from .views import category_add, category_list, category_detail, category_change, category_delete

urlpatterns = [
    path('category/',category_list),
    path('category-detail/<int:pk>/',category_detail),
    path('category-add/',category_add),
    path('category-change/<int:pk>/', category_change),
    path('category-delete/<int:pk>/', category_delete),
]