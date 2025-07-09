from django.http import HttpResponse, JsonResponse
from .models import Project, Tareas
from django.shortcuts import get_object_or_404,render
# Create your views here.
def index (request):
    title = "Bienvenido a Curso de Django !"
    return render(request,"index.html",{
        "title" : title
    })
    
def variableabout(request):
    username ="Guxo"
    return render(request,"about.html",{
        "username" : username
    })


def variablehola (request,username):
    return HttpResponse("<h2>Hola %s</h2>" % username)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all() # type: ignore
    return render(request, "projects.html",{
        "projects" : projects
    })

def tareas(request):
    # tarea = Tareas.objects.get(title=title)
    tareas = Tareas.objects.all() # type: ignore
    return render(request, "tareas.html",{
        "tareas" : tareas
    })    
