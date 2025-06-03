from django.shortcuts import render

# Create your views here.
from .forms import miFormulario, LogForm
from django.http import HttpResponse
from .models import Menu

#vista_1
def suma (request):
    x = 56
    y = 4
    suma = x+y
    return HttpResponse("La suma de " + str(x) + " + " + str(y) + " es igual a " + str(suma))

def muestras (request, tipo_muestra):
    muestra = {
        'bovinos' : 'De animales del rancho de la FESC',
        'felinos' : 'Gatos de gente que ingresan en el hospital de FESC',
        'caninos' : 'Perros de gente que ingresan en el hospital de FESC',
    }
    
    eleccion_de_muestra = muestra[tipo_muestra]
    return HttpResponse(f"<h1>{tipo_muestra}</h1>" + eleccion_de_muestra)

#Parametros de consulta
def qryview(request):
    if request.method == "POST":
        id = request.POST['id']
        nombre = request.POST['nombre']
    elif request.method == "GET":
        id = request.POST['id']
        nombre = request.POST['nombre']
    return HttpResponse("Nombre:{} Id_usuario:{}".format(nombre, id))

#parametros de ruta
def pathview(request, nombre, id):  
        return HttpResponse("Nombre:{} Id_usuario:{}".format(nombre, id))
    
# Renderizar html
def muestra_formulario(request):
    return render(request, "form.html")

#Obtener datos del formulario
def getform(request):
    if request.method == "POST":
        id = request.POST['id']
        nombre = request.POST['nombre']
    return HttpResponse("Nombre:{} Id_usuario:{}".format(nombre, id))    

def datos_view(request):
    if request.method == 'POST':
        form = miFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            edad = form.cleaned_data['edad']
            return render(request, 'exito.html', {'nombre':nombre, })
    else:
            form = miFormulario()
            
    return render(request, 'formulario.html', {'form':form})

def logform(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save() #Guardar datos en base de datos
    contexto = {'form':form}
    return render(request, 'login.html', contexto)

