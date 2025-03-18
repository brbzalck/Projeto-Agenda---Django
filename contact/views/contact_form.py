from django.shortcuts import render
from contact.forms import ContactForm

# função de requisição que renderiza a criação de dados
def create(request):
    # se o usuário entrar com dados == POST
    if request.method == 'POST':
        # enviando para o context os dados obtidos de POST
        context = {
            'form': ContactForm(request.POST)
        }

        # se action form = True, renderiza novamente o create com os dados preenchidos
        return render(
        request,
        'contact/create.html',
        context,
    )

    # se não existir entrada de dados, apenas acesso ao create
    context = {
        # envia os campos em branco para preenchimento
        'form': ContactForm()
    }

    # renderiza a requisição com a resposta create vazia para preenchimento
    return render(
        request,
        'contact/create.html',
        context,
    )