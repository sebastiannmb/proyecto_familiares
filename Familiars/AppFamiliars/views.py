from django.shortcuts import render
from django.http import HttpResponse
from AppFamiliars.models import Familiars, Profession

def create_familiar(request):
    new_familiar = Familiars.objects.create(name= 'Oscar Rivas', edad=56, genero=True)
    print(new_familiar)
    return HttpResponse('Se agregó el familiar')

def list_familiars(request):
    all_familiars = Familiars.objects.all()
    print(all_familiars)
    context = {
        'familiars':all_familiars,
    }
    return render(request, 'list_familiars.html', context=context)

def create_profession(request, name):
    Profession.objects.create(name=name)
    return HttpResponse('Profesión creada')

def list_professions(request):
    all_professions = Profession.objects.all()
    context = {
        'professions':all_professions
        }
    return render(request, 'list_professions.html', context=context)