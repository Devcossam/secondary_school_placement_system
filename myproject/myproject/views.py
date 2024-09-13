from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home_page(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())