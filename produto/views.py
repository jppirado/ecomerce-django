from django.shortcuts import render , reverse , redirect

from carrosapp.models import Supplier
from .models import Product
from .forms import ProductForm

# Create your views here.

def createProduct( request  ):
    data = {}
    data ['data'] = ProductForm()
    return render( request, 'produto/form_suppliers.html', data)

def cadastrar( request):
    form = ProductForm(request.POST or None)
    if form.is_valid( ):
        form.save( )
    return  redirect('/')
   
def listar(request):
  produtos = Product.objects.all()
  return render( request , "produto/list_product.html" , {'produtos' :produtos}) 
