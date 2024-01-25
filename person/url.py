from django.urls import path
from .views import *

urlpatterns = [
    # ------- client urls start  ----- #

    path('client/', client_list),
    path('client-add/', client_add),
    path('client-change/<int:pk>/', client_change),
    path('client-detail/<int:pk>/', client_detail),
    path('client-delete/<int:pk>/', client_delete),

    # ------- client urls end  ----- #

    # ------- client urls start  ----- #

    path('employee/', employee_list),
    path('employee-add/', employee_add),
    path('employee-change/<int:pk>/', employee_change),
    path('employee-detail/<int:pk>/', employee_detail),
    path('employee-delete/<int:pk>/', employee_delete),

    # ------- client urls end  ----- #
]