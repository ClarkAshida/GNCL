from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import UserEditForm

@method_decorator(login_required, name='dispatch')
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('funcionarios')
    template_name = 'cadastrarFuncionario.html'

@login_required
def funcionarios(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        funcionarios = User.objects.filter(username__icontains=search)
    elif filter:
        funcionarios = User.objects.all().order_by(filter)
    else:
        funcionarios_list = User.objects.all()
        paginator = Paginator(funcionarios_list, 10)
        page = request.GET.get('page')
        funcionarios = paginator.get_page(page)
    return render(request, 'funcionarios.html', {'funcionarios': funcionarios})


@login_required
def display_funcionarios(request, id=None):
    if id:
        funcionarios_id = User.objects.get(id=id)
    else: 
        funcionarios_id = "" 
    return render(request, 'funcionarios_id.html', {"funcionarios_id": funcionarios_id})

@login_required
def editarFuncionario(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Funcionário Editado com sucesso.')
            return redirect('funcionarios')
    else:
        form = UserEditForm(instance=user)

    return render(request, 'editarFuncionario.html', {'form': form})

@login_required
def deletarFuncionario(request, id):
    funcionarios_id = get_object_or_404(User, pk=id)
    funcionarios_id.delete()
    messages.info(request, 'Funcionário deletada com sucesso.')
    return redirect('funcionarios')