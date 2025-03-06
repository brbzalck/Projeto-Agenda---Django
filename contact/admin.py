from django.contrib import admin
# importando os models de contact para acessar o model Contact
from contact import models

# Register your models here.

# registrando Contact pelo decoretor admin.register(recebe o model)
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # criando classe que recebe decoretor(e recebe admin.ModelAdmin)
    ...