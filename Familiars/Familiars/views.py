
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def vista_con_template(request):
    return render(request, 'template.html', context={})




