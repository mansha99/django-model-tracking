from django.shortcuts import render
import random
from django.http import HttpResponse
from .models import Stock
def index(request):
    r=random.randint(0,1)
    s =Stock.objects.get(pk=1)
    if(r==0):
        s.current_value=s.current_value+1
    else: 
        s.current_value=s.current_value-1
    s.save()
    return HttpResponse('Updated')
def chat_room(request):
    return render(request, 'chat.html')