from django.shortcuts import render, redirect, get_object_or_404
from.models import Linguagem,Exercicio,Crianca
from.forms import CriancaForm



def index(request):
    linguagens = Linguagem.objects.all()
    return render(request,'polls/index.html',{'linguagens':linguagens})

def detalhe(request,linguagem_id):
    linguagem = get_object_or_404(Linguagem,pk=linguagem_id)
    return render(request,'polls/detalhe.html',{'linguagem':linguagem})

def quiz(request,linguagem_id):
    linguagem = get_object_or_404(Linguagem,pk=linguagem_id)
    exercicios = Exercicio.objects.filter(linguagem=linguagem)
    return render(request,'polls/quiz.html',{
        'linguagem':linguagem,
        'exercicios': exercicios
    })

def resultado(request, linguagem_id):
    linguagem = get_object_or_404(Linguagem, pk=linguagem_id)
    exercicios = Exercicio.objects.filter(linguagem=linguagem)
    acertos = 0
    total = exercicios.count()
    for exercicio in exercicios:
        resposta_dada = request.POST.get(f'resposta_{exercicio.id}')
        if resposta_dada == exercicio.resposta_correta:
            acertos += 1
    return render(request, 'polls/resultado.html', {
        'linguagem': linguagem,
        'acertos': acertos,
        'total': total,
    })

def cadastro(request):
    if request.method == 'POST':
        form = CriancaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'polls/cadastro_sucesso.html')
    else:
        form = CriancaForm()
    return render(request, 'polls/cadastro.html', {'form': form})
    
def login(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        crianca = Crianca.objects.filter(nome__iexact=nome).first()
        if crianca:
            request.session['crianca_id'] = crianca.id
            return redirect('resultado', linguagem_id=crianca.linguagem.id)
        else:
            return render(request, 'polls/login.html', {'erro': 'Nome não encontrado. Verifica ou cadastra-te primeiro.'})
    return render(request, 'polls/login.html')