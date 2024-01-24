from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia
from datetime import date
from .forms import NoticiaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

@login_required
def cadastrarnoticia(request):
    if request.method == "GET":
        form = NoticiaForm()
        return render(request, 'noticias/cadastrarNoticia.html', {'form': form})
    elif request.method == "POST":
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia = Noticia(
                titulo=form.cleaned_data['titulo'],
                autor=request.user,
                texto=form.cleaned_data['texto'],
                legenda=form.cleaned_data['legenda'],
                categoria=form.cleaned_data['categoria'],
                data_e_hora=date.today(),
                id_funcionario=request.user
            )
            noticia.save()
            messages.info(request, 'Notícia criada com sucesso.')
            return redirect('noticias')
        else:
            return render(request, 'noticias/cadastrarNoticia.html', {'form': form})

@login_required
def noticias(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    autorFilter = request.GET.get('autorFilter')
    funcionarios = get_user_model().objects.all()

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

@login_required
def display_noticias(request, id=None):
    if id:
        noticias_id = Noticia.objects.get(id=id)
    else: 
        noticias_id = "" 
    return render(request, 'noticias/noticias_id.html', {"noticias_id": noticias_id})

@login_required
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

@login_required
def deletarNoticia(request, id):
    noticias_id = get_object_or_404(Noticia, pk=id)
    noticias_id.delete()
    messages.info(request, 'Notícia deletada com sucesso.')
    return redirect('noticias')


    