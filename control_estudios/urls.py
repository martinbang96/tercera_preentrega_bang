from django.contrib import admin
from django.urls import path

from control_estudios.views import (
    listar_cursos, crear_curso, buscar_cursos,listar_estudiantes,crear_estudiante, buscar_estudiantes,listar_profesores,crear_profesor,buscar_profesores
)

# Son las URLS especificas de la app
urlpatterns = [
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),

    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path("crear-estudiante/", crear_estudiante, name="crear_estudiante"),
    path("buscar-estudiante/", buscar_estudiantes, name="buscar_estudiantes"),
    
    path("profesores/", listar_profesores, name="lista_profesores"),
    path("crear-profesor/", crear_profesor, name="crear_profesor"),
    path("buscar-profesor/", buscar_profesores, name="buscar_profesores"),
]
