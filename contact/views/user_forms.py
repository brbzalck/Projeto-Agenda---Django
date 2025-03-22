from django.shortcuts import render, redirect
from contact.forms import RegistrerForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm

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
            return redirect('contact:login')

    # retorna como resposta de requisição, o html de register com o form de RegistrerForm
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

# view de atualização de usuários
def user_update(request):
    # criando o formulário que é auto-preenchido com os dados do usuário logado
    form = RegisterUpdateForm(instance=request.user)

    # se não for o método post
    if request.method != 'POST':
        # retorna como resposta de requisição, o html de register com o form de RegistrerUpdateForm
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )
    
    # mudando o form caso seja POST, (com os novos dados de entrada, no determinado usuário)
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    # se o formulário não for válido
    if not form.is_valid():
        # retorna como resposta de requisição, o html de register com o form de RegistrerUpdateForm
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )
    
    # salva os dados no banco de dados
    form.save()
    # retorna como resposta de requisição a própria view de update
    return redirect('contact:user_update')

# view de login
def login_view(request):
    # que pega os campos de AuthenticationForm já prontos
    form = AuthenticationForm(request)

    # se tiver entrada de dados
    if request.method == 'POST':
        # preencher o form com os dados vindos de POST
        form = AuthenticationForm(request, data=request.POST)

        #  se o formulário for válido primeiramente
        if form.is_valid():
            # pega qual é esse usuário
            user = form.get_user()
            # faz o login dele com a senha vindas do post
            auth.login(request, user)
            # manda uma mensagem no base do site
            messages.success(request, 'Logado com sucesso!')
            # como retorno redireciona para index 
            return redirect('contact:index')
        # se chegar aqui é pq deu merda exibi msg de erro
        messages.error(request, 'Login inválido')
            

    #  se for apenas get exibi o login normal com o form em branco
    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

# função de logout
def logout_view(request):
    # desloga o usuário autenticado atualmente
    auth.logout(request)
    # redireciona para login denovo
    return redirect('contact:login')