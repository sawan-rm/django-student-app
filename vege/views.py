from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def receipes(request):
    
    if request.method == 'POST':

        data = request.POST
        receipe_img = request.FILES.get('receipe_img')
        receipe_name = data.get('receipe_name')
        receipe_descrioption = data.get('receipe_descrioption')

        Recepie.objects.create(
            receipe_name=receipe_name,
            receipe_descrioption=receipe_descrioption,
            receipe_img=receipe_img,
        )

        return redirect('/receipes/')

    querySet = Recepie.objects.all()

    context = {'receipes': querySet}

    return render(request, 'receipes.html', context)