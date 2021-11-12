from django.shortcuts import render
from .models import contactlist
from .models import contactform
from django.contrib import messages

# Create your views here.

def contactus(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactformdata = contactform(name=name, email=email, subject=subject, message=message)
        contactformdata.save()

    contactlistdata = contactlist.objects.all()[0]

    context = {
        'contactlist' : contactlistdata,
    }
    messages.success(request, 'Message sent successfully successfully')

    return render(request,'contact.html',context)
