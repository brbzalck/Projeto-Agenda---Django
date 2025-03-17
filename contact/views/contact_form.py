from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator

from contact.models import Contact


def create(request):
    # se o método for post executa isso
    if request.method == 'POST':
        print()
        print(request.method)
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))
        print()

    context = {

    }

    print()
    # verificando método caso não tenha nenhum input no Send(post)
    print(request.method)
    print()

    return render(
        request,
        'contact/create.html',
        context,
    )