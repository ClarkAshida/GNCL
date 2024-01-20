from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Funcionario, Noticia
from datetime import date
from .forms import NoticiaForm, FuncionarioForm
from django.contrib import messages

def cadastrarfuncionario(request):
    if request.method == "GET":
        form = FuncionarioForm()
        return render(request, 'funcionarios/cadastro.html', {'form': form})
    elif request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = Funcionario(
            name = form.cleaned_data['name'],
            login = form.cleaned_data['login'],
            password = form.cleaned_data['password']
            )
            funcionario.save()
            return redirect('funcionarios')
        else:
            return render(request, 'funcionarios/cadastro.html', {'form': form})

def funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/funcionarios.html', {'funcionarios': funcionarios})

def cadastrarnoticia(request):
    if request.method == "GET":
        form = NoticiaForm()
        return render(request, 'noticias/cadastrarNoticia.html', {'form': form})
    elif request.method == "POST":
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia = Noticia(
                titulo=form.cleaned_data['titulo'],
                autor=Funcionario.objects.get(id='1').name,
                texto=form.cleaned_data['texto'],
                legenda=form.cleaned_data['legenda'],
                categoria=form.cleaned_data['categoria'],
                data_e_hora=date.today(),
                id_funcionario=Funcionario.objects.get(id='1')
            )
            noticia.save()
            return redirect('noticias')
        else:
            return render(request, 'noticias/cadastrarNoticia.html', {'form': form})

def noticias(request):
    noticias = Noticia.objects.all().order_by('-data_e_hora')
    return render(request, 'noticias/noticias.html', {'noticias': noticias})

def login(request):
    return render(request, 'funcionarios/login.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def display_funcionarios(request, id=None):
    if id:
        funcionarios_id = Funcionario.objects.get(id=id)
    else: 
        funcionarios_id = "" 
    return render(request, 'funcionarios/funcionarios_id.html', {"funcionarios_id": funcionarios_id})

def display_noticias(request, id=None):
    if id:
        noticias_id = Noticia.objects.get(id=id)
    else: 
        noticias_id = "" 
    return render(request, 'noticias/noticias_id.html', {"noticias_id": noticias_id})

def editarNoticia(request, id=None):
    noticias_id = get_object_or_404(Noticia, pk=id)
    form = NoticiaForm(instance=noticias_id)

    if request.method == "POST":
        form = NoticiaForm(request.POST, instance=noticias_id)
        if(form.is_valid()):
            noticias_id.save()
            return redirect('noticias')
        else:
            return render(request, "noticias/editarNoticia.html", {'form':form, 'noticias_id':noticias_id})
    else:
        return render(request, "noticias/editarNoticia.html", {'form':form, 'noticias_id':noticias_id})

def deletarNoticia(request, id):
    noticias_id = get_object_or_404(Noticia, pk=id)
    noticias_id.delete()
    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('noticias')




    