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
