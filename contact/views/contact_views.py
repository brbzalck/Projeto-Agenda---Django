from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact

# view que pega a requisição index e retorna a renderização como resposta determinado html
def index(request):
    # variável que guarda todos os dados contido em Contact
    contacts = Contact.objects.filter(show=True).order_by('-id')

    # colocando os objetos coletados no dict context para fins de exportação render
    context = {
        # esse contact pode ser iterado -> é um objeto com vários objetos
        'contacts': contacts,
        # passando no contexto um valor para site_title
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        # index retorna todos os dados de Contact para ser manipulado
        context,
    )

# definindo oque a view search vai fazer
def search(request):
    # pegando valores do método get e guardando numa variável
    search_value = request.GET.get('q', '').strip()
    
    # se esse valor for vazio retorna a página inicial
    if search_value == '':
        return redirect('contact:index')

    # pesquisando dentro da table Contact objetos que estão com show=True em determinas colunas
    contacts = Contact.objects\
        .filter(show=True)\
            .filter(Q(first_name__icontains=search_value) |
                    # utilizando a class Q para conseguir fazer a query no sql com OR representado por |
                    Q(last_name__icontains=search_value) |
                    Q(phone__icontains=search_value) |
                    Q(email__icontains=search_value)
                    )\
                .order_by('-id')

    # passando o resultado da query para o contexto e o novo título da página atual
    context = {
        'contacts': contacts,
        'site_title': 'Search - '
    }

    return render(
        request,
        # retornando a própria view de index só que com o context específico da consulta da query search
        'contact/index.html',
        # contexto que retorna apenas oque o get pedir e a query retornar
        context,
    )

# criando a view contact, que recebe a "requisição" com o "contato_id" passado pela urls como parâmetro
def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()

    # get_object tenta pegar o objeto caso contrário da 404
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    # Pegando da tabela Contact, a pk que seja = contact_id, e que esteja com show ok

    # criando uma variável para atribuir os valores para a chave site_title
    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '

    # context armazena os dados em contact para serem repassados para o template
    context = {
        'contact': single_contact,
        # passando no contexto um valor para site_title
        'site_title': contact_name
    }

    # retorna a requisição, joga para o template desejado, e com o contexto para uso
    return render(
        request,
        # retorna a página de contact
        'contact/contact.html',
        # manda os dados do contact para utilização
        context
    )
