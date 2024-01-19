from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario, Noticia
from datetime import date

def cadastrarfuncionario(request):
    if request.method == "GET":
        return render(request, 'funcionarios/cadastro.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        login = request.POST.get('login')
        password = request.POST.get('password')
        funcionario = Funcionario(
            name = name,
            login = login,
            password = password
        )
        funcionario.save()
        return render(request, 'funcionarios/cadastro.html')

def funcionarios(request):
    funcionarios = Funcionario.objects.all()
    print(funcionarios[0].name)
    return render(request, 'funcionarios/funcionarios.html', {'funcionarios': funcionarios})

def cadastrarnoticia(request):
    if request.method == "GET":
        return render(request, 'noticias/cadastrarNoticia.html')
    elif request.method == "POST":

        author = request.POST.get('author')
        title = request.POST.get('title')
        caption = request.POST.get('caption')
        category = request.POST.get('category')
        text = request.POST.get('text')

        noticia = Noticia(
            titulo = title,
            autor = author,
            texto = text,
            legenda = caption,
            categoria = category,
            data_e_hora = date.today(),
            id_funcionario = Funcionario.objects.filter(id = '1')[0]
        )
        noticia.save()
        print(noticia)
        return render(request, 'noticias/cadastrarNoticia.html')

def noticias(request):
    noticias = Noticia.objects.all()
    print(noticias[0].titulo)
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
    