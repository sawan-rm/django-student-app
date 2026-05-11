from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    students = [
        {
            "name": "Rahul",
            "age": 21
        },
        {
            "name": "Aman",
            "age": 22
        },
        {
            "name": "Priya",
            "age": 20
        },
        {
            "name": "Neha",
            "age": 23
        },
        {
            "name": "Karan",
            "age": 2
        }
    ]
    # for st in students:
    #     print(st)
        
    return render(request, 'website/index.html', context={'students': students})

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')
