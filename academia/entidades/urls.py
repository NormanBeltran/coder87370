from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name="home"),
    
    # ____ Cursos
    path("cursos/", cursos, name="cursos"),
    path("cursoForm/", cursoForm, name="cursoForm"),
    path("cursoUpdate/<id>/", cursoUpdate, name="cursoUpdate"),
    path("cursoDelete/<id>/", cursoDelete, name="cursoDelete"),

    # ____ Profesores
    path("profesores/", profesores, name="profesores"),
    path("profesorForm/", profesorForm, name="profesorForm"),
    path("profesorUpdate/<id>/", profesorUpdate, name="profesorUpdate"),
    path("profesorDelete/<id>/", profesorDelete, name="profesorDelete"),
    
    # ____ Estudiantes
    path("estudiantes/", EstudianteListView.as_view(), name="estudiantes"),
    path("estudianteCreate/", EstudianteCreateView.as_view(), name="estudianteCreate"),
    path("estudianteUpdate/<int:pk>/", EstudianteUpdateView.as_view(), name="estudianteUpdate"),
    path("estudianteDelete/<int:pk>/", EstudianteDeleteView.as_view(), name="estudianteDelete"),
    
    
    # ____ Entregables
    path("entregables/", entregables, name="entregables"),
]
