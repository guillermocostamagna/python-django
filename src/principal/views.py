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
    from datetime import datetime
    
    año_actual = datetime.now().year
    contexto = {"año":año_actual}
    return render(request, "principal/index.html", contexto)

def tirar_dado(request):
    from datetime import datetime
    from random import randint

    tiro_de_dado = randint(1,6)
    
    if tiro_de_dado == 6:
        mensaje = f'Has tirado el dado y has sacado {tiro_de_dado}! Ganaste!'
    else:
        mensaje = f'Has tirado el dado y has sacado {tiro_de_dado}! Sigue intentando! Presiona F5'
        
    datos = {
        'title' : "Tiro de dados",
        'message' : mensaje,
        'fecha' : datetime.now().strftime('%H:%M:%S:%f'),
    }
    return render(request, 'principal/dados.html', context=datos)
        