from django.shortcuts import render, redirect
from contact.forms import RegistrerForm
from django.contrib import messages

def register(request):
    # func register, pega os campos padrões de RegisterForm
    form = RegistrerForm()

    # se o método for POST, pega os dados e salva do DB
    if request.method == 'POST':
        form = RegistrerForm(request.POST)

        if form.is_valid():
            form.save()
            # assim que salvar exibi mensagem de sucess na requisição de 'Usuário registrado'
            messages.success(request, 'Usuário registrado')
            # retorna como redirecionamento o index ao salvar enviar contato em create
            return redirect('contact:index')

    # retorna como resposta de requisição, o html de register com o form de RegistrerForm
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )