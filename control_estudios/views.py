from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from control_estudios.models import Curso, Estudiante,Profesor
from control_estudios.forms import CursoFormulario,EstudianteFormulario,ProfesorFormulario

def listar_estudiantes(request):
    contexto = {
        "estudiantes": Estudiante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response

def crear_estudiante(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            apellido = data["apellido"]
            nombre = data["nombre"]
            dni = data["dni"]
           
            estudiante = Estudiante(apellido=apellido, nombre=nombre, dni=dni)
            # Lo guardan en la Base de datos
            estudiante.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_estudiantes')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = EstudianteFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_estudiante.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_estudiantes(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        estudiantes = Estudiante.objects.filter(apellido__contains=busqueda)
        # Ejemplo filtro avanzado
        # cursos = Curso.objects.filter(
        #     Q(nombre=busqueda) | Q(comision__contains=busqueda)
        # )
        contexto = {
            "estudiantes": estudiantes,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_estudiantes.html',
            context=contexto,
        )
        return http_response


def listar_profesores(request):
    contexto = {
        "profesores": Profesor.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_profesores.html',
        context=contexto,
    )
    return http_response

def crear_profesor(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            apellido = data["apellido"]
            nombre = data["nombre"]
            dni = data["dni"]
            profesion = data["profesion"]
    
            profesor = Profesor(apellido=apellido,nombre=nombre, dni=dni,profesion=profesion)
            # Lo guardan en la Base de datos
            profesor.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_profesores')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProfesorFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_profesor.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_profesores(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        profesores = Profesor.objects.filter(apellido__contains=busqueda)
        # Ejemplo filtro avanzado
        # cursos = Curso.objects.filter(
        #     Q(nombre=busqueda) | Q(comision__contains=busqueda)
        # )
        contexto = {
            "profesores": profesores,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_profesores.html',
            context=contexto,
        )
        return http_response



def listar_cursos(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "cursos": Curso.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response

def crear_curso(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            comision = data["comision"]
            # creo un curso en memoria RAM
            curso = Curso(nombre=nombre, comision=comision)
            # Lo guardan en la Base de datos
            curso.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_cursos')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = CursoFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_curso.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_cursos(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        cursos = Curso.objects.filter(comision__contains=busqueda)
        # Ejemplo filtro avanzado
        # cursos = Curso.objects.filter(
        #     Q(nombre=busqueda) | Q(comision__contains=busqueda)
        # )
        contexto = {
            "cursos": cursos,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_cursos.html',
            context=contexto,
        )
        return http_response
