from django.shortcuts import render


# view que pega a requisição index e retorna a renderização como resposta determinado html
def index(request):
    return render(
        request,
        'contact/index.html',
    )