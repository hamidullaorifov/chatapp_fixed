from django import views
from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('',views.index,name='index'),
    path('getChats/<int:id>',views.getChats,name='getChats'),
    path('getMessages/',views.getMessages,name='getMessages'),
    path('chatting/<int:id>',views.chatting,name='chatting'),
    path('send/',views.send,name='send'),
    path('getContacts/',views.getContacts,name='getContacts')
]
