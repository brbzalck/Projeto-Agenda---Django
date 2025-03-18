from django import forms
from django.core.exceptions import ValidationError
from . import models

# Criando form baseado no Model django
class ContactForm(forms.ModelForm):
    class Meta:
        # definindo qual model se trata
        model = models.Contact
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
