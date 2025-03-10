import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

# definindo o caminho da pasta raiz do projeto
DJANGO_BASE_DIR = Path(__file__).parent.parent
# constante para definir quantos contatos irão criar
NUMBER_OF_OBJECTS = 1000

# adicionando a raiz do projeto ao sys.path para o python encontrar por módulos(project.settings)
sys.path.append(str(DJANGO_BASE_DIR))
# os.environ para guardar variáveis de ambiente, usado aqui para informar qual módulo de configuração usar no django
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
# desabilitando o tz para não precisar configurar aqui
settings.USE_TZ = False

# carrega o django com essas configurações
django.setup()

# só executa se executar o módulo diretamente
if __name__ == '__main__':
    import faker

    # importando category e contact de models
    from contact.models import Category, Contact

    # deletando todos os contatos e categorias do model
    Contact.objects.all().delete()
    Category.objects.all().delete()

    # fazendo a preterencia de dados em pt_BR
    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    # atribuindo novas categorias para Category retirada da lista categories por meio de LC
    django_categories = [Category(name=name) for name in categories]

    # para cada categoria das novas adicionadas, save.
    for category in django_categories:
        category.save()

    # lista vazia para manipulação
    django_contacts = []

    # iterando de 01 até 1000
    for _ in range(NUMBER_OF_OBJECTS):
        # criando um perfil pela biblioteca faker
        profile = fake.profile()
        # retirando email fake dos dados de prefile fake
        email = profile['mail']
        # atribuindo nome e sobrenome respectivamente separados pelo espaço
        first_name, last_name = profile['name'].split(' ', 1)
        # criando um numero fake
        phone = fake.phone_number()
        # criando uma data fake relativa a este ano
        created_date: datetime = fake.date_this_year()
        # criando um texto de descrição fake relativo a esse ano
        description = fake.text(max_nb_chars=100)
        # escolhendo uma categoria aleatória para o contato atual
        category = choice(django_categories)

        # adicionando contatos ao django adm
        django_contacts.append(
            Contact(
                # atribuindo os dados fakes gerados aos dados de criação(na memoria)
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    # se os contatos for maior que 0, cria os contatos
    if len(django_contacts) > 0:
        # criando os contatos que estão na memoria de uma vez
        Contact.objects.bulk_create(django_contacts)