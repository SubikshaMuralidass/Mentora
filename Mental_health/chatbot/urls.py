'''from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    
    
    
    path('', views.chatbot_view, name='chatbot'),
    path('send_message/', views.send_message, name='send_message'),
    path('clear_chat/', views.clear_chat, name='clear_chat'),
]'''
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.chatbot_home, name='chatbot_home'),
    path("chat_page/", views.chat_page, name="chat_page"),
    path("send_message/", views.send_message, name="send_message"),
    #path("dashboard/", views.dashboard, name="dashboard"),  # if you have a dashboard
]
