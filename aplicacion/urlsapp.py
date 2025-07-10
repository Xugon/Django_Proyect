from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('about/', views.variableabout,name="about"),
    path("hola/<str:username>",views.variablehola,name="hola"),
    path('project/', views.projects,name="projects"),
    path('tareas/', views.tareas,name="tareas"),
    path('create_task/', views.create_task,name="create_task")
]