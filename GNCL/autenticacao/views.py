from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario, Noticia
from datetime import date

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/cadastro.html')
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
        return render(request, 'cadastro/index.html')

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
    return HttpResponse('Faça seu Login')