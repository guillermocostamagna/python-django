from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    return HttpResponse("Hola Guille!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Hola Guillo!!!!<h1>")

def saludar_con_paramtros(request, nombre:str, apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"Hola {nombre} {apellido} desde jango con paramtros!!!")

def index(request):
    return render(request, "principal/index.html")
