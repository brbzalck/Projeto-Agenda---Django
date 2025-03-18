from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact

# Criando form baseado no Model django
class ContactForm(forms.ModelForm):
    class Meta:
        # definindo qual model se trata
        model = Contact
        # selecioanando as columns ta table
        fields = (
            'first_name', 'last_name', 'phone',
        )

    # função clean que pega os dados limpos do POST
    def clean(self):
        cleaned_data = self.cleaned_data

        # adicionando um erro propositalmente
        self.add_error(
            # em first_name
            'first_name',
            # com essa mensagem e código de erro
            ValidationError('Mensagem Erro', code='invalid')
        )
        self.add_error(
            'first_name',
            ValidationError('Mensagem Erro 2', code='invalid')
        )

        return super().clean()


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