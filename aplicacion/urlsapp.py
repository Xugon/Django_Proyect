from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path('about/', views.variableabout),
    path("hola/<str:username>",views.variablehola),
    path('project/', views.projects),
    path('tareas/', views.tareas)
]