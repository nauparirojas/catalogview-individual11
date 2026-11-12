
from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


# Vista basada en función (FBV)
def home(request):
    contexto = {
        'titulo': 'Bienvenido',
        'mensaje': 'Sistema de catálogo tecnológico de la UNCP'
    }
    return render(request, 'catalogo/home.html', contexto)


# Vista basada en clase (CBV)
class ProductoListView(ListView):
    model = Producto
    template_name = 'catalogo/catalogo.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.filter(
            stock__gte=0
        ).order_by('nombre')
