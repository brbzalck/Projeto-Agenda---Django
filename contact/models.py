from django.db import models
from django.utils import timezone

# Create your models here.
# SEMPRE QUE TIVER ALTERAÇÕES NO MODELS ==
# == python manage.py makemigrations - irá criar as migrações na pasta migrations

# python manage.py migrate ==  para migrar de fato os models para o Banco de Dados

# id (primary_key - automático pelo django)

# Criando tabela de categorias para usar como ForeignKey
class Category(models.Model):
    class Meta:
        # Nome que aparece quando há uma categoria apenas
        verbose_name = 'Category'
        # nome que aparece quando aparecer p clicar em categorias disponíveis
        verbose_name_plural = 'Categories'
    # única coluna que existe na tabela é name
    name = models.CharField(max_length=50)

    # função que retorna na instância do obejto a string com first e last name
    def __str__(self):
        # esse retorno irá ser o nome da categoria na adm do django
        return self.name

class Contact(models.Model):
    ### criando colunas da tabela contact
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # email é obrigatório para registro, porem se tiver blank não é mais obrigatório
    email = models.EmailField(max_length=254, blank=True)
    # criando a data automática default= pelo metódo de timezone
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    # campo show que começa automaticamente com True
    show = models.BooleanField(default=True)
    # campo para fotos que pode ser nulo e vai ser salvo com o caminho de upload_to
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    # coluna categoria que é uma ForeignKey que vem da tabela Category
    category = models.ForeignKey(
        Category,
        # qual deletar deixar nulo o vínculo
        on_delete=models.SET_NULL,
        # não é obrigatório e pode ser nulo para complementar on_delete
        blank=True, null=True
        )

    # função que retorna na instância do obejto a string com first e last name
    def __str__(self):
        # esse retorno irá ser o nome do contato na adm do django
        return f'{self.first_name} {self.last_name}'
