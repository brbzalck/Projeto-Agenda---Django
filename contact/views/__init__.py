# sempre que as views forem requisitadas, irá carregar todas as views importadas nesse init
from .contact_views import *
# colocando as views criadas separadamente para iniciar com __init quando forem requisitadas
from .contact_form import *
from .user_forms import *