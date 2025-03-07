### python manage.py shell - para inicial o shell do django ###

#  primeiramene importamos a model
from contact.models import Contact

# Criando um contato pelo shell que vai direto para base de dados
c = Contact.objects.create(first_name='Pedrin', last_name='matador')

# Criando uma instância de Contact com first_name(precisa de c.save)
c = Contact(first_name='Charles')

# depois de instanciado da para adicionar direto atributos ao model
c.last_name = 'Bronx'

# após realizar o CRUD, c.save() para salvar na base de dados/django ADM
c.save()

# para deletar a instância da base de dados
c.delete()
# mesmo despois de deletar, a instância continua na memória podendo ser recupearda

############################################

# usando o método get de objects que foi herdado ao Contact
# método responsável por pegar na base de dados objeto com (atributo=x)
c = Contact.objects.get(id=4)

# exibe id do objeto selecionado
c.id
# exibe primarey_key do objeto selecionado
c.pk

############################################

# usando método all de objects que foi herdado ao Contact
# método retorna todos os objetos em um QuerySet
c = Contact.objects.all()

# iterando essa QuerySet com for que exibi o nome de todos
for contato in c: contato.first_name

############################################

# usando método filter de objects que foi herdado ao Contact
# método que filtra o atributo argumentado em uma QuerySet
c = Contact.objects.filter(id=4)

############################################

# selecionando todos os contatos e ordenando pelo id
c = Contact.objects.all().order_by('-id')

# para fechar o shell :)
quit()