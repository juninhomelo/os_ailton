from services.models import Service
from services.forms import ServiceModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ServiceListView(ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class ServiceCreateView(CreateView):
    model = Service
    template_name = 'services_create.html'
    form_class = ServiceModelForm
    success_url = reverse_lazy('services')


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services_detail.html'


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceModelForm
    template_name = 'services_update.html'

    def get_success_url(self):
        return reverse_lazy('services_detail', kwargs={'pk': self.object.pk})


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'services_delete.html'
    success_url = '/services/'
