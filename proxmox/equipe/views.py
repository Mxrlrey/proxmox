from django.shortcuts import render, redirect
from .forms import EquipeForm
from .models import Equipe

def cadastro_equipe(request):
    if request.method == "POST":
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('list')  
    else:
        form = EquipeForm()
    
    return render(request, "equipe/cadastro.html", {"form": form})

def list(request):
    equipes = Equipe.objects.all()
    return render(request, "equipe/listar_equipes.html", {"equipes": equipes})
