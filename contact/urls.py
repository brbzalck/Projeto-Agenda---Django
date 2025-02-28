from django.urls import path

from contact import views

app_name = 'contact'

# onde fica mapeado as url
urlpatterns = [
    # 'index do site', execução da função, nomeando a URL
    path('', views.index, name='index'),
]