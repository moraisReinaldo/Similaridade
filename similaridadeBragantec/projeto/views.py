from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from .models import Projeto
 
def paginaI (request):
    projetos = Projeto.objects.all()
    
    busca = request.GET.get('search')
    if busca:
        projetos = Projeto.objects.filter(titulo__icontains = busca)

        
    return render(request,'index.html',{'projetos': projetos})

def verProjeto (request, codigo):
    projeto = get_object_or_404(Projeto, pk=codigo)
    return render(request,'projetos/projeto.html',{'projeto': projeto})


