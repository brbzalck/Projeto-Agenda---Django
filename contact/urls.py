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
    # adicionando url que recebe id de deleção
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    # url de criação, que puxa a execução a view create, de nome create
    path('contact/create/', views.create, name='create'),

    # USER
    
    # url para criação de usuário que puxa a view register
    path('user/create/', views.register, name='register'),
    # url para login, view que puxa a func login_view, de nome login
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),

]