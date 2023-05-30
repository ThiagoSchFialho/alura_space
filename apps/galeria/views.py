from django.shortcuts import render, get_object_or_404, redirect

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForm

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

def add_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = FotografiaForm()
    if request.method == 'POST': 
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem salva com sucesso!')
            return redirect('index')
        else :
            messages.erro(request, 'Ocorreu um erro na salvamento da nova imagem')
            return redirect('add_imagem')

    return render(request, 'galeria/add_imagem.html', {"form": form})

def editar_imagem(request):
    return render(request, 'galeria/editar_imagem.html')

def deletar_imagem(request):
    return render(request, 'galeria/deletar_imagem.html')

