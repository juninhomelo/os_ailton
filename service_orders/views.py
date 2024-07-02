from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from service_orders.models import ServiceOrder
from service_orders.forms import ServiceOrderModelForm


class ServiceOrderListView(ListView):
    model = ServiceOrder
    template_name = 'service_orders.html'
    context_object_name = 'service_orders'


class ServiceOrderCreateView(CreateView):
    model = ServiceOrder
    template_name = 'service_orders_create.html'
    form_class = ServiceOrderModelForm
    success_url = reverse_lazy('service_orders')

