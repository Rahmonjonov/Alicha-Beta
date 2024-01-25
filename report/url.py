from django.urls import path
from .views import *

urlpatterns = [

    # ------- order url start ------- #

    path('order/', order_list),
    path('order-add/<int:pk>/', order_add),
    path('order-detail/<int:pk>/', order_detail),
    path('order-delete/<int:pk>/', order_delete),

    # ----- order url end --------- #

    # ------- checkout  url start ------- #

    path('checkout/', checkout_list),
    path('checkout-add/', checkout_add),
    path('checkout-delete/<int:pk>/', checkout_destroy),
    path('checkout-today/', today_checkout),

    # ----- checkout url end --------- #

]