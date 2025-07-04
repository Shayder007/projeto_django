from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'menu-principal.html')

def cadastro(request):
    return render(request, 'tela-cadastro.html')