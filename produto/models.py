from django.db import models
from carrosapp.models import Supplier 

# Create your models here.

class Product( models.Model ):
    name_product = models.CharField( max_length=70)
    quantity_product = models.IntegerField( ) 
    fornecedor = models.ForeignKey(Supplier , on_delete=models.CASCADE)

    def __str__(self):
        return self.name_product

    def __str__(self):
        return self.quantity_product  

    
        

