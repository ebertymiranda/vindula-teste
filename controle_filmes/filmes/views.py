from django.shortcuts import render, redirect
from .models import Filme
from .forms import FilmeForm
from .tasks import importar_planilha_excel
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage


def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista_filmes.html', {'filmes': filmes})

def cadastra_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm()
    return render(request, 'filmes/cadastra_filme.html', {'form': form})


def handle_uploaded_file(file):
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    return fs.url(filename)

def importa_excel(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file_path = handle_uploaded_file(request.FILES['file'])
    
        importar_planilha_excel.delay(file_path)
        
        return render(request, 'filmes/importa_excel.html', {'mensagem': 'Importação iniciada. Aguarde a conclusão.'})

    return render(request, 'filmes/importa_excel.html')


def lista_filmes_autocomplete(request):
    termo_pesquisa = request.GET.get('term', '')
    filmes = Filme.objects.filter(nome__icontains=termo_pesquisa)
    lista_filmes = [filme.nome for filme in filmes]
    return JsonResponse(lista_filmes, safe=False)


def relatorio_filmes(request):
    filmes_assistidos = Filme.objects.filter(data_assistido__isnull=False)
    filmes_nao_assistidos = Filme.objects.filter(data_assistido__isnull=True, gostaria_assistir=False)
    filmes_desejados = Filme.objects.filter(gostaria_assistir=True)

    return render(request, 'filmes/relatorio_filmes.html', {
        'filmes_assistidos': filmes_assistidos,
        'filmes_nao_assistidos': filmes_nao_assistidos,
        'filmes_desejados': filmes_desejados,
    })
