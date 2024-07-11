from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from service_orders.models import ServiceOrder, Brand
from service_orders.forms import ServiceOrderModelForm, BrandModelForm


class ServiceOrderListView(ListView):
    model = ServiceOrder
    template_name = 'service_orders.html'
    context_object_name = 'service_orders'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        client_name = self.request.GET.get('name')
        model = self.request.GET.get('model')

        if client_name:
            queryset = queryset.filter(client__name__icontains=client_name)
        
        if model:
            queryset = queryset.filter(model__icontains=model)

        return queryset


class ServiceOrderCreateView(CreateView):
    model = ServiceOrder
    template_name = 'service_orders_create.html'
    form_class = ServiceOrderModelForm
    success_url = reverse_lazy('service_orders')


class ServiceOrderDetailView(DetailView):
    model = ServiceOrder
    template_name = 'service_orders_detail.html'


class ServiceOrderUpdateView(UpdateView):
    model = ServiceOrder
    form_class = ServiceOrderModelForm
    template_name = 'service_orders_update.html'

    def get_success_url(self):
        return reverse_lazy('service_orders_detail', kwargs={'pk': self.object.pk})


class ServiceOrderDeleteView(DeleteView):
    model = ServiceOrder
    template_name = 'service_orders_delete.html'
    success_url = '/service_orders/'


def generate_pdf(request, pk):
    object = get_object_or_404(ServiceOrder, pk=pk)
    html_string = render_to_string('pdf.html', {'object': object})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=OS_{object.id}.pdf'

    pisa_status = pisa.CreatePDF(html_string, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some erros <pre>' + html_string + '</pre>')
    return response


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandModelForm
    success_url = reverse_lazy('brand_create')


class BrandListView(ListView):
    model = Brand
    template_name = 'brand_create.html'
    context_object_name = 'brands'
