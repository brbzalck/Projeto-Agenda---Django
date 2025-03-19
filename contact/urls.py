from django.urls import path

from contact import views

app_name = 'contact'

# onde fica mapeado as url
urlpatterns = [
    # 'index do site', execução da função, nomeando a URL
    path('', views.index, name='index'),
    # url requisitada pelo form, que puxa view search, de nome search
    path('search/', views.search, name='search'),
    
    # CONTACT CRUD
    
    # url de endereço manda o contact_id como parâmetro, chama a view contact, com nome de url contact
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    # criando nova url de atualização do contato
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    # url de criação, que puxa a execução a view create, de nome create
    path('contact/create/', views.create, name='create'),
]