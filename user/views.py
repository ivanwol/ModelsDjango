from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person


def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})


def create(request):
    if request.method == 'POST':
        people = Person()
        people.name = request.POST.get('name')
        people.surname = request.POST.get('surname')
        people.age = request.POST.get('age')
        people.phone = request.POST.get('phone')
        people.save()
    return HttpResponseRedirect('/')