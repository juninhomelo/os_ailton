from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from customers.models import Client
from customers.forms import ClientModelForm


class ClientListView(ListView):
    model = Client
    template_name = 'customers.html'
    context_object_name = 'customers'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class ClientCreateView(CreateView):
    model = Client
    template_name = 'customers_create.html'
    form_class = ClientModelForm
    success_url = reverse_lazy('customers')


class ClientDetailView(DetailView):
    model = Client
    template_name = 'customers_detail.html'


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientModelForm
    template_name = 'customers_update.html'

    def get_success_url(self):
        return reverse_lazy('customers_detail', kwargs={'pk': self.object.pk})


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'customers_delete.html'
    success_url = '/customers/'