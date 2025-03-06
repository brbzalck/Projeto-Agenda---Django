from django.db import models
from django.utils import timezone

# Create your models here.
# SEMPRE QUE TIVER ALTERAÇÕES NO MODELS ==
# == python manage.py makemigrations - irá criar as migrações na pasta migrations

# python manage.py migrate ==  para migrar de fato os models para o Banco de Dados

# id (primary_key - automático pelo django)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # email é obrigatório para registro, porem se tiver blank não é mais obrigatório
    email = models.EmailField(max_length=254, blank=True)
    # criando a data automática default= pelo metódo de timezone
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    # função que retorna na instância do obejto a string com first e last name
    def __str__(self):
        # esse retorno irá ser o nome do contato na adm do django
        return f'{self.first_name} {self.last_name}'
