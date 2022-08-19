from ctypes import FormatError
from django.shortcuts import render
from django.views.generic import TemplateView , CreateView , ListView , DeleteView , UpdateView
from .forms import SupplierForm
from .models import Supplier



class IndexView( TemplateView ):
    template_name = 'index.html'

class CarsCreateview( CreateView ):
        model = Supplier
        form_class = SupplierForm
        success_url = '/'

class CarsListView( ListView ):
    model = Supplier
    queryset = Supplier.objects.all()

class CarsDeleteView( DeleteView ):
    model = Supplier 
    success_url = '/'

class  CarsEditView (UpdateView):
    model = Supplier
    form_class = SupplierForm
    success_url = '/'

