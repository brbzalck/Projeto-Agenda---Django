from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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
        return email

# personalizando meu form de atualização de usuário
class RegisterUpdateForm(forms.ModelForm):
    # personalizando campo de first_name
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )
    # personalizando campo de senha1
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
 
    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )   
     
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    # função de atualizar/validar email
    def clean_email(self):
        # pegando qual email existe no form(POST)
        email = self.cleaned_data.get('email')
        # pegando qual email existe na base de dados
        current_email = self.instance.email

        # se um for diferente do outro é pq o user quer atualizar
        if current_email != email:
            # se já existe um email igual na base de dados levanta erro
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )
        # retorna qual email irá manter no formulário
        return email

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError:
                ...
        return password1