from django.shortcuts import render
from contact.models import Contact

# view que pega a requisição index e retorna a renderização como resposta determinado html
def index(request):
    # variável que guarda todos os dados contido em Contact
    contacts = Contact.objects.all()

    # colocando os objetos coletados no dict context para fins de exportação render
    context = {
        # esse contact pode ser iterado -> é um objeto com vários objetos
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        # index retorna todos os dados de Contact para ser manipulado
        context
    )
