from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from service_orders.models import ServiceOrder
from service_orders.forms import ServiceOrderModelForm


class ServiceOrderCreateView(CreateView):
    model = ServiceOrder
    template_name = 'service_orders_create.html'
    form_class = ServiceOrderModelForm
    success_url = reverse_lazy('customers')
