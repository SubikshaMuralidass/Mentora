from django.urls import path
from . import views

urlpatterns = [
    #path('', views.test_home, name='test_home'),
    path('test/', views.take_test, name='take_test'),
    path('submit/', views.submit_test, name='submit_test'),]
