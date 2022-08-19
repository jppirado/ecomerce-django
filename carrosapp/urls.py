from django.urls import path
from .views import CarsCreateview, CarsListView, IndexView , CarsDeleteView,   CarsEditView

urlpatterns = [

    path('' , IndexView.as_view(), name='home'),
    path('create/' , CarsCreateview.as_view(), name='create'),
    path('list/' , CarsListView.as_view(), name='create'),
    path('<int:pk>/delete/' , CarsDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit/' ,  CarsEditView.as_view(), name='editar')

]