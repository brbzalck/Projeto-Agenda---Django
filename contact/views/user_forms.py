from django.shortcuts import render
from contact.forms import RegistrerForm

def register(request):
    # func register, pega os campos padrões de RegisterForm
    form = RegistrerForm()

    # se o método for POST, pega os dados e salva do DB
    if request.method == 'POST':
        form = RegistrerForm(request.POST)

        if form.is_valid():
            form.save()

    # retorna como resposta de requisição, o html de register com o form de RegistrerForm
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )