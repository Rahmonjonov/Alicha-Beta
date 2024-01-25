from django.urls import path
from .views import *

urlpatterns = [

    # ---------- story about url start -------------- #

    path('story-about/', story_about_list),
    path('story-about-add/', story_about_add),
    path('story-about-change/<int:pk>/', story_about_change),
    path('story-about-detail/<int:pk>/', story_about_detail),
    path('story-about-delete/<int:pk>/', story_about_delete),

    # ---------- story about url start -------------- #

    # ---------- dept market url start -------------- #

    path('dept-market/', dept_market_list),
    path('dept-market-add/', dept_market_add),
    path('dept-market-change/<int:pk>/', dept_market_change),
    path('dept-market-detail/<int:pk>/', dept_market_change),
    path('dept-market-delete/<int:pk>/', dept_market_delete),

    # ---------- dept market url start -------------- #

    # ---------- dept market url start -------------- #

    path('cost/', cost_list),
    path('cost-add/', cost_add),
    path('cost-change/<int:pk>/', cost_change),
    path('cost-detail/<int:pk>/', cost_detail),
    path('cost-delete/<int:pk>/', cost_delete),

    # ---------- dept market url start -------------- #

]