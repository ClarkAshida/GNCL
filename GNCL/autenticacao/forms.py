from django import forms
from .models import Funcionario, Noticia

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['name', 'login', 'password']

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome do Funcionário'}))
    login = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nome do Funcionário'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Senha do Funcionário'}))

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'legenda', 'categoria', 'texto']
        
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Título da Notícia'}))
    legenda = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Legenda da Notícia'}))
    categoria = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Categoria da Notícia'}))
    texto = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Texto da Notícia'}))