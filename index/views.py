from django.shortcuts import render
from .models import about,slider,client

# Create your views here.
def home(request):
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    clientdata = client.objects.all()
    context = {
        'about' : aboutdata,
        'slider' : sliderdata,
        'client' : clientdata

    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')
