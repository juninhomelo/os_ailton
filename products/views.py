from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from products.models import Product
from products.forms import ProductModelForm


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products_create.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'products_update.html'

    def get_success_url(self):
        return reverse_lazy('products_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products_delete.html'
    success_url = '/products/'
