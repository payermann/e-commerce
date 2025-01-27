from django.views import generic
from .models import Product

class IndexView(generic.ListView):
    model = Product
    template_name = 'index.html'
    paginate_by = 20
    context_object_name = 'products'
