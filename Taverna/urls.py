from django.urls import path
from Taverna.views import(
    home,
    tables,
    users,
    about,
    not_implemented,
    add_user,
    search_user,
    add_new,
    add_table
)

urlpatterns = [
path('', home, name='home'),
path('agregar_noticia/', add_new, name='add_new'),
path('mesas/', tables, name='tables'),
path('agregar_mesa/', add_table, name='add_table'),
path('usuarios/', users, name='users'),
path('usuarios/<message_in>', users, name='users'),
path('agregar_usuario/', add_user, name='add_user'),
path('buqueda_usuario/', search_user, name='search_user'),
path('descripcion/', about, name='about'),
path('no_implementado/', not_implemented, name='not_i'),

]