from django.http import HttpResponse
from django.template import Template, Context, loader

from app.models import *
import datetime, random

def saludar(request):
    return HttpResponse("¡Hola, mundo! Esta es una vista desde Django.")

def bienvenido(request, nombre, apellido):
    return HttpResponse(f"¡Bienvenido a mi sitio web, {nombre} {apellido}!")

def bienvenido_html(request, nombre, apellido):
    hoy = datetime.datetime.now()
    html_content = f"""
    <html>
        <head>
            <title>Bienvenida</title>
        </head>
        <body>
            <h1>¡Bienvenido a mi sitio web, {nombre} {apellido}!</h1>
            <h2>Nos alegra tenerte aquí.</h2>
            <h3>Explora y disfruta de nuestro contenido.</h3>
            <h4>Siéntete como en casa.</h4>
            <p>Estamos encantados de tenerte aquí.</p>
            <p>Fecha y hora de acceso: {hoy}</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)

def bienvenido_tpl(request, nombre, apellido):
    hoy = datetime.datetime.now()

    with open("C:/Coderhouse/87370/clase_11_12_13/proyecto/proyecto/plantillas/bienvenida.html", "r", encoding="utf-8") as file:
        template = Template(file.read())
        contexto = Context({"nombre": nombre, "apellido": apellido, "hoy": hoy})
        html_content = template.render(contexto)

    return HttpResponse(html_content)

def bienvenido_tpl2(request, nombre, apellido):
    hoy = datetime.datetime.now()
    notas = [4,3,6,7, 8, 9, 10]
    contexto = {"nombre": nombre, "apellido": apellido, "hoy": hoy, "notas": notas}
    plantilla = loader.get_template("bienvenida2.html")
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

def nuevo_curso(request):
    nro_comision = random.randint(1000, 2999)
    nombre_curso = f"Python {nro_comision}"
    curso = Curso(nombre=nombre_curso, comision=nro_comision)
    curso.save()
    return HttpResponse(f"Curso '{curso.nombre}' de la comisión {curso.comision} creado exitosamente.")
