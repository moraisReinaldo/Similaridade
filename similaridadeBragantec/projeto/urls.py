from django.urls import path

from . import views

urlpatterns = [
    path('', views.paginaI, name = 'paginaI'),
    path('projeto/<int:codigo>', views.verProjeto, name = "verProjeto"),

]

