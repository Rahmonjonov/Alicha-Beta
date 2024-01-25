from django.urls import path
from .views import *


urlpatterns = [

    path('sign-in/', sign_in),
    path('sign-up/', sign_up),
    path('logout/', user_logout),
]