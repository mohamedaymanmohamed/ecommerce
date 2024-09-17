from django.shortcuts import render
from .models import Login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    data = Login(username=username, password=password)
    
    
    return render(request, 'payment.html')



