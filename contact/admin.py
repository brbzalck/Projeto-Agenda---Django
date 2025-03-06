from django.contrib import admin
# importando os models de contact para acessar o model Contact
from contact import models

# Register your models here.

# registrando Contact pelo decoretor admin.register(recebe o model)
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # criando classe que recebe decoretor(e recebe admin.ModelAdmin)
    list_display = 'id', 'first_name', 'last_name', 'phone',
    # ordenando por
    ordering = '-id',
    # barra de pesquisa para os colunas determinadas
    search_fields = 'id', 'first_name', 'last_name',
    # 10 por página
    list_per_page = 10
    # max de 100 por página
    list_max_show_all = 200
    # opção do adm editar direto o argumetos da tupla
    list_editable = 'first_name', 'last_name',
    # colocando os argumentos como link de acesso ao dado
    list_display_links = 'id', 'phone',