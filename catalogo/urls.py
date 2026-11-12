
from django.urls import path
from .views import home, ProductoListView

urlpatterns = [
    path('', home, name='home'),
    path('catalogo/', ProductoListView.as_view(), name='catalogo'),
]
