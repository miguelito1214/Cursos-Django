from django.shortcuts import render, HttpResponse

menu="""
    <a href="/">Home</a>
    <a href="/cursos">Cursos</a>
    <a href="/contacto">Contacto</a>
"""

def principal(request):
    contenido="<h1>BIENVENIDO A MI SITIO WEB</h1>"
    return render(request,"contenido/principal.html")

def cursos(request):
  return render(request,"contenido/formulario.html")

def contacto(request):
   return render(request,"contenido/contacto.html")