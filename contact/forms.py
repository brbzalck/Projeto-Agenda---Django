from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Criando form baseado no Model django
class ContactForm(forms.ModelForm):
    # editando como quero que o campo picture fique
    picture = forms.ImageField(
        # permetindo upload de arquivos
        widget=forms.FileInput(
            # aceitando apenas imagens
            attrs={
                'accept': 'image/*'
            }
        )
    )


    class Meta:
        # definindo qual model se trata
        model = models.Contact
        # selecioanando os atributos da model(table)
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category', 'picture',
        )

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

# criando minha própria classe para registro de usuário
class RegistrerForm(UserCreationForm):
    # colocando os campos de registros como obrigatórios
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    # editando caracteristicas dos campos form
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        # meu model é User que já tem pronto no django p criar Usuário
        model = User
        # selecionando quais campos eu vou querer
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2'
        )

    # 
    def clean_email(self):
        # pegando o campo email preenchido no formulário
        email = self.cleaned_data.get('email')

        # se em usuários com filtro de email=email já existir determinado email
        if User.objects.filter(email=email).exists():
            # sobe erro para o usuário
            self.add_error(
                # no campo email
                'email',
                # com essa mensagem e código
                ValidationError('Já existe este e-mail', code='invalid')
            )