from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms


def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms()
    contexto = {'form': form, 'pessoa_form':pessoa_form}
    return render(request, 'index.html', contexto)


def revisao_consulta(request):
    if request.method == "POST":
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        contexto = {'form': form, 'pessoa_form':pessoa_form}
        if form.is_valid():
            return render(request, 'minha_consulta.html', contexto)
        else:
            print("Erro no formulário")
            return render(request, 'index.html', contexto)

