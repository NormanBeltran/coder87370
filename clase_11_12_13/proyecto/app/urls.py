from django.urls import path, include

from .views import *

urlpatterns = [
    path("saludo/", saludar),
    path("bienvenido/<str:nombre>/<str:apellido>/", bienvenido),
    path("bienvenido_html/<str:nombre>/<str:apellido>/", bienvenido_html),
    path("bienvenido_tpl/<str:nombre>/<str:apellido>/", bienvenido_tpl),
    path("bienvenido_tpl2/<str:nombre>/<str:apellido>/", bienvenido_tpl2),
    path("nuevo_curso/", nuevo_curso),
]
