from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Funcionario, Noticia
from datetime import date
from .forms import NoticiaForm, FuncionarioForm
from django.contrib import messages
from django.core.paginator import Paginator

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
            messages.info(request, 'Funcionário criado com sucesso.')
            return redirect('funcionarios')
        else:
            return render(request, 'funcionarios/cadastro.html', {'form': form})

def funcionarios(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        funcionarios = Funcionario.objects.filter(name__icontains=search)
    elif filter:
        funcionarios = Funcionario.objects.all().order_by(filter)
    else:
        funcionarios_list = Funcionario.objects.all()
        paginator = Paginator(funcionarios_list, 3)
        page = request.GET.get('page')
        funcionarios = paginator.get_page(page)
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
                autor=Funcionario.objects.get(id='2').name,
                texto=form.cleaned_data['texto'],
                legenda=form.cleaned_data['legenda'],
                categoria=form.cleaned_data['categoria'],
                data_e_hora=date.today(),
                id_funcionario=Funcionario.objects.get(id='2')
            )
            noticia.save()
            messages.info(request, 'Notícia criada com sucesso.')
            return redirect('noticias')
        else:
            return render(request, 'noticias/cadastrarNoticia.html', {'form': form})

def noticias(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    autorFilter = request.GET.get('autorFilter')
    funcionarios = Funcionario.objects.all()

    if search:
        noticias = Noticia.objects.filter(titulo__icontains=search)
    elif filter:
        noticias = Noticia.objects.all().order_by(filter)
    elif autorFilter:
        noticias = Noticia.objects.filter(autor__icontains=autorFilter)
    else:
        noticias_list = Noticia.objects.all().order_by('-data_e_hora')
        paginator = Paginator(noticias_list, 3)
        page = request.GET.get('page')
        noticias = paginator.get_page(page)
    return render(request, 'noticias/noticias.html', {'noticias': noticias, "funcionarios": funcionarios})

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
            messages.info(request, 'Notícia editada com sucesso.')
            return redirect('noticias')
        else:
            return render(request, "noticias/editarNoticia.html", {'form':form, 'noticias_id':noticias_id})
    else:
        return render(request, "noticias/editarNoticia.html", {'form':form, 'noticias_id':noticias_id})

def deletarNoticia(request, id):
    noticias_id = get_object_or_404(Noticia, pk=id)
    noticias_id.delete()
    messages.info(request, 'Notícia deletada com sucesso.')
    return redirect('noticias')

def editarFuncionario(request, id=None):
    funcionarios_id = get_object_or_404(Funcionario, pk=id)
    form = FuncionarioForm(instance=funcionarios_id)

    if request.method == "POST":
        form = FuncionarioForm(request.POST, instance=funcionarios_id)
        if(form.is_valid()):
            funcionarios_id.save()
            messages.info(request, 'Funcionário editado com sucesso.')
            return redirect('funcionarios')
        else:
            return render(request, "funcionarios/editarFuncionario.html", {'form':form, 'funcionarios_id':funcionarios_id})
    else:
        return render(request, "funcionarios/editarFuncionario.html", {'form':form, 'funcionarios_id':funcionarios_id})

def deletarFuncionario(request, id):
    funcionarios_id = get_object_or_404(Funcionario, pk=id)
    funcionarios_id.delete()
    messages.info(request, 'Funcionário deletada com sucesso.')
    return redirect('funcionarios')



    