from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
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


def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.surname = request.POST.get('surname')
            person.age = request.POST.get('age')
            person.phone = request.POST.get('phone')
            person.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Page not found</h2>')


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Page not found</h2>')