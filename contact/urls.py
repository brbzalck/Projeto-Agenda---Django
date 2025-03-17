from django.urls import path

from contact import views

app_name = 'contact'

# onde fica mapeado as url
urlpatterns = [
    # url manda o contact_id como parâmetro, chama a view contact, com nome de url contact
    path('<int:contact_id>/', views.contact, name='contact'),
    # url requisitada pelo form, que puxa view search, de nome search
    path('search/', views.search, name='search'),
    # 'index do site', execução da função, nomeando a URL
    path('', views.index, name='index'),
]