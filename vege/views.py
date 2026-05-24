from django.shortcuts import render, redirect, get_object_or_404
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

    search_query = request.GET.get('search')

    if search_query:
        querySet = querySet.filter(
            receipe_name__icontains=search_query
        )

    context = {
        'receipes': querySet,
        'search_query': search_query
    }

    return render(request, 'receipes.html', context)


def delete_receipe(request, id):
    receipe = get_object_or_404(Recepie, id=id)
    receipe.delete()
    return redirect('/receipes')


def update_receipe(request, id):

    receipe = get_object_or_404(Recepie, id=id)

    if request.method == 'POST':
        receipe.receipe_name = request.POST.get('receipe_name')
        receipe.receipe_descrioption = request.POST.get('receipe_descrioption')

        if request.FILES.get('receipe_img'):
            receipe.receipe_img = request.FILES.get('receipe_img')

        receipe.save()
        return redirect('/receipes/')

    context = {'receipe': receipe}

    return render(request, 'update_receipes.html', context)
