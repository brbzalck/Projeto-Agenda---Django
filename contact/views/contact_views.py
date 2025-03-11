from django.shortcuts import render, get_object_or_404
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
