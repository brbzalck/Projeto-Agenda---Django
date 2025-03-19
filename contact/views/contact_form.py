from django.shortcuts import render, redirect
from contact.forms import ContactForm

# função de requisição que renderiza a criação de dados
def create(request):
    # se o usuário entrar com dados == POST
    if request.method == 'POST':
        # salvando os dados obtidos pelo POST
        form = ContactForm(request.POST)
        # enviando para o context os dados obtidos de POST
        context = {
            'form': form
        }
        # se o formulário estiver válido
        if form.is_valid():
            # salva na base de dados
            form.save()
            # e redireciona para a view create
            return redirect('contact:create')


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