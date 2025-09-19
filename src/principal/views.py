from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    return HttpResponse("Hola Guille!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Hola Guillo!!!!<h1>")