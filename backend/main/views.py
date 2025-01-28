from django.views import generic
from .models import Product, Action

class IndexView(generic.ListView):
    model = Product
    template_name = 'index.html'
    paginate_by = 20
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actions'] = Action.objects.all()
        return context

class ProductView(generic.DetailView):
    model = Product
    template_name = 'product.html'

class ActionView(generic.DetailView):
    model = Action
    template_name = 'action.html'

class ProductListView(generic.ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 30
    context_object_name = 'products'
