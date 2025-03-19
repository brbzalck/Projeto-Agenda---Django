from django import forms
from django.core.exceptions import ValidationError
from . import models

# Criando form baseado no Model django
class ContactForm(forms.ModelForm):
    # editando a column first_name da model com widget para atributos na label
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Escreva aqui'
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda',
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # pegando pelo init do contactForm o first_name e modificando com widgets

        # self.fields['first_name'].widget.attrs.update({
        #     'placeholder': 'Escreva aqui!'
        # })

    class Meta:
        # definindo qual model se trata
        model = models.Contact
        # selecioanando as columns ta table
        fields = (
            'first_name', 'last_name', 'phone',
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Escreva aqui'
        #         }
        #     )
        # }

    # função clean que pega os dados limpos do POST(tem acesso a tds campos do form)
    def clean(self):
        # usando cleaned_data no objeto para acessar os campos do form
        cleaned_data = self.cleaned_data
        # pegando os valores de entrada nos campos first e last name
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            # criando msg de erro com ValidationError para add.error
            msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid',
                )
            # adicionando erro ao campo first_name, com determinada mensagem
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        # método clean retorna super().clean() para fazer quantas validações forem precisas
        return super().clean()

    # função clean para campo específico que retorna o próprio campo
    def clean_first_name(self):
        # pegando os dados limpos do POST onde o campo for = first_name
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            # adicionando um erro no objeto
            self.add_error(
            # em first_name
            'first_name',
            # com essa mensagem e código de erro
            ValidationError('Mensagem Erro 2', code='invalid')
        )

        # método epecifico de clean_campo retorna o próprio campo para manter no form como exemplo
        return first_name
