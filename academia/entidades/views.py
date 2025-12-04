from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

def profesores(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)

def estudiantes(request):
    contexto = {"estudiantes": Estudiante.objects.all()}
    return render(request, "entidades/estudiantes.html", contexto)

def entregables(request):
    contexto = {"entregables": Entregable.objects.all()}
    return render(request, "entidades/entregables.html", contexto)

def cursoForm(request):
    if request.method == "POST":
        miFormulario = CursoForm(request.POST) # Aqui me llega toda la informacion del formulario
        if miFormulario.is_valid():
            curso_nombre = miFormulario.cleaned_data.get("nombre")
            curso_comision = miFormulario.cleaned_data.get("comision")
            curso_profesor = miFormulario.cleaned_data.get("profesor")
            curso = Curso(nombre=curso_nombre, comision=curso_comision, profesor=curso_profesor)
            curso.save()
            contexto = {"cursos": Curso.objects.all()}
            return render(request, "entidades/cursos.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacío
        miFormulario = CursoForm()

    contexto = { "form": miFormulario}
    return render(request, "entidades/cursoForm.html", contexto)

def cursoUpdate(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        miFormulario = CursoForm(request.POST) # Aqui me llega toda la informacion del formulario
        if miFormulario.is_valid():
            curso.nombre = miFormulario.cleaned_data.get("nombre")
            curso.comision = miFormulario.cleaned_data.get("comision")            
            curso.profesor = miFormulario.cleaned_data.get("profesor")            
            curso.save()
            contexto = {"cursos": Curso.objects.all()}
            return render(request, "entidades/cursos.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacío
        miFormulario = CursoForm(initial={"nombre": curso.nombre, "comision": curso.comision})

    contexto = { "form": miFormulario}
    return render(request, "entidades/cursoForm.html", contexto)

def cursoDelete(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

# Profesores
def profesorForm(request):
    if request.method == "POST":
        miFormulario = ProfesorForm(request.POST) # Aqui me llega toda la informacion del formulario
        if miFormulario.is_valid():
            profesor_nombre = miFormulario.cleaned_data.get("nombre")
            profesor_apellido = miFormulario.cleaned_data.get("apellido")
            profesor_email = miFormulario.cleaned_data.get("email")
            profesor_profesion = miFormulario.cleaned_data.get("profesion")
            profesor = Profesor(nombre=profesor_nombre, apellido=profesor_apellido, email=profesor_email, profesion=profesor_profesion)
            profesor.save()
            contexto = {"profesores": Profesor.objects.all()}
            return render(request, "entidades/profesores.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacío
        miFormulario = ProfesorForm()

    contexto = { "form": miFormulario}
    return render(request, "entidades/profesorForm.html", contexto)

def profesorUpdate(request, id):
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        miFormulario = ProfesorForm(request.POST) # Aqui me llega toda la informacion del formulario
        if miFormulario.is_valid():
            profesor.nombre = miFormulario.cleaned_data.get("nombre")
            profesor.apellido = miFormulario.cleaned_data.get("apellido")            
            profesor.email = miFormulario.cleaned_data.get("email")            
            profesor.profesion = miFormulario.cleaned_data.get("profesion")            
            profesor.save()
            contexto = {"profesores": Profesor.objects.all()}
            return render(request, "entidades/profesores.html", contexto)
    else:
        # Es la primer vez que se ingresa al formulario
        # Se crea un formulario vacío
        miFormulario = ProfesorForm(initial={"nombre": profesor.nombre, "apellido": profesor.apellido, "email": profesor.email, "profesion": profesor.profesion})

    contexto = { "form": miFormulario}
    return render(request, "entidades/profesorForm.html", contexto)

def profesorDelete(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)