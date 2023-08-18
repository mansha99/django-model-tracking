# urls.py

from django.urls import path
from stock.views import chat_room,index

urlpatterns = [
    # Other paths...
    path('', index),
    path('chat/', chat_room, name='chat_room'),
    
]