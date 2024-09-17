from django.shortcuts import render
from django.http import HttpResponse

 def home(request):
     return HttpResponse('Welcome to my website!')

 def about(request):
     return HttpResponse('This is my about page.')


 def payment(request):
     return render(request, 'temolates/payment.html')



