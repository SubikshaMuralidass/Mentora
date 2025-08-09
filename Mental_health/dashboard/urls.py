from django.urls import path
from . import views

urlpatterns = [
    #path('', views.dashboard_home, name='dashboard'), 
    #path('', views.dashboard_home, name='dashboard_home'),
    path('insights/', views.dashboard_insights, name='dashboard_insights'),
]
