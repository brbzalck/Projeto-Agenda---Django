from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact
from django.contrib.auth.decorators import login_required

# função de requisição que renderiza a criação de contatos
# so poderá criar contatos se estiver logado
@login_required(login_url='contact:login')
def create(request):
    # armazena a URL que iremos mandar o formulário
    form_action = reverse('contact:create')
    # se o usuário entrar com dados == POST
    if request.method == 'POST':
        # salvando os dados obtidos pelo POST e os arquivos
        form = ContactForm(request.POST, request.FILES)
        # enviando para o context os dados obtidos de POST
        context = {
            # form preenchido
            'form': form,
            # colocando a URL de destino do form no contexto
            'form_action': form_action,
        }
        # se o formulário estiver válido
        if form.is_valid():
            # cria o contato, mas não salva ainda na base da dados
            contact = form.save(commit=False)
            # atribuindo proprietário de criação do contato
            contact.owner = request.user
            # por fim salvando
            contact.save()
            # e redireciona para a view update, com id resgatado de Contact
            return redirect('contact:update', contact_id=contact.pk)


        # se enviar e der falha, renderiza novamente para edição
        return render(
        request,
        'contact/create.html',
        context,
    )

    # se não existir entrada de dados, apenas acesso ao create
    context = {
        # envia os campos em branco para preenchimento
        'form': ContactForm(),
        'form_action': form_action,
    }

    # renderiza a requisição com a resposta create vazia para preenchimento
    return render(
        request,
        'contact/create.html',
        context,
    )

# decorater que só exibe a view se o user estiver logado
@login_required(login_url='contact:login')
def update(request, contact_id):
    # pegando o contato da table Contact, onde a pk é igual ao id recebido pelo redirect de create
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    # colocando proprietário requisitado para atualizar o contato

    # salvando URL de destino do form, com contato selecionado para atualização
    form_action = reverse('contact:update', args=(contact_id,))
    # se o usuário entrar com dados == POST
    if request.method == 'POST':
        # atualizando com instance=contact, os novos dados vindo do POST no ID certo
        form = ContactForm(request.POST, request.FILES, instance=contact)
        # colocando arquivos dentro do form para manipulação

        # enviando para o context os dados obtidos de POST
        context = {
            # form preenchido
            'form': form,
            # para onde ele vai ir
            'form_action': form_action,
        }
        # se o formulário estiver válido
        if form.is_valid():
            # salva na base de dados
            contact = form.save()
            # e redireciona para a view update, com id resgatado de Contact(pk)
            return redirect('contact:update', contact_id=contact.pk)
            # caimos num loop, sempre que salvar puxa o próprio update novamente


        # se enviar e der falha, renderiza novamente para edição
        return render(
        request,
        'contact/create.html',
        context,
    )

    # se não existir entrada de dados, apenas resgata os dados de determinado ID para edição
    context = {
        # enviando os campos preenchidos por instance=contact que resgata os dados
        'form': ContactForm(instance=contact),
        # contexto puxa o próprio update para edição
        'form_action': form_action,
    }

    # renderiza a requisição com a resposta create vazia para preenchimento
    return render(
        request,
        'contact/create.html',
        context,
    )

# função da view delete
# decorater que só exibe a view se o user estiver logado
@login_required(login_url='contact:login')
def delete(request, contact_id):
    # tenta achar o objeto requerido primeiro
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    # colocando proprietário requisitado para deleção de contato

    # pega qual estado de confirmation
    confirmation = request.POST.get('confirmation', 'no')

    # se confirmation for yes pelas 2 etapas, exclui contato
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )