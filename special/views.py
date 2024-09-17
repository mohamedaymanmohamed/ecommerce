from django.shortcuts import render
from .models import Specialy

# Create your views here.

def index(request):
    username = request.POST.get('username')
    print(username)
    
    
    return render(request, 'payment.html', {'shika': Specialy.objects.all()})


def about(request):
    
    
    
    return render(request, 'about.html')