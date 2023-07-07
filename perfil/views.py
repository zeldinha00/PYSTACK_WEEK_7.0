from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contas, Categoria
from django.contrib import messages
from django.contrib.messages import constants
from .utils import calcula_total

# pagina HOME
def home(request):
    contas = Contas.objects.all()
    saldo_total = calcula_total(contas, 'valor')
    return render(request, 'home.html', {'contas': contas, 'saldo_total': saldo_total,})


# Suas Contas
def gerenciar(request):
    # enviar para o html as contas
    contas = Contas.objects.all()
    # enviar para o html as categorias
    categorias = Categoria.objects.all()
    saldo_total = calcula_total(contas, 'valor')
    return render(request, 'gerenciar.html', {'contas': contas, 'saldo_total': saldo_total, 'categorias': categorias})



# função para pegar os dados digitados e colocar no banco de dados
def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    
    # validar o apelido
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/perfil/gerenciar/')

    conta = Contas(
        apelido = apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()

    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso')

    return redirect('/perfil/gerenciar/')

def deletar_banco(request, id):
    conta = Contas.objects.get(id=id)
    conta.delete()
    
    messages.add_message(request, constants.SUCCESS, 'Conta removida com sucesso')
    return redirect('/perfil/gerenciar/')

def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    categoria = Categoria(
        categoria=nome,
        essencial=essencial
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso')
    return redirect('/perfil/gerenciar/')

def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    categoria.essencial = not categoria.essencial

    categoria.save()

    return redirect('/perfil/gerenciar/')