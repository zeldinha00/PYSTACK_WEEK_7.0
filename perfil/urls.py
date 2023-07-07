from django.urls import path
from  . import views

urlpatterns = [
    # www.meusite.com.br/perfil/home
    path('home/', views.home, name='home'),
    # pagina Gerenciar
    path('gerenciar/', views.gerenciar, name='gerenciar'),
    # pagina cadastrar_conta
    path('cadastrar_banco/', views.cadastrar_banco, name="cadastrar_banco"),
    # pagina para deletar uma conta
    path('deletar_banco/<int:id>', views.deletar_banco, name="deletar_banco"),
    # pagina cadastrar categoria
    path('cadastrar_categoria/', views.cadastrar_categoria, name="cadastrar_categoria"),
    # pagina para update nas categorias
    path('update_categoria/<int:id>', views.update_categoria, name="update_categoria"),

]
