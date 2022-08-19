from django.urls import path

from .views import createProduct , cadastrar , listar 

urlpatterns = [
    path('' , createProduct , name='product.list'), 
    path('add/' , cadastrar , name='product.add'),
    path('listar' ,listar , name='produto.list'),
]