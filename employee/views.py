from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employee(request):
    data = 'This is the employee page'
    return HttpResponse(data)
def profile(request):
    return render(request,'employee/profile.html')
