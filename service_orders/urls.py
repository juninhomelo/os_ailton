from django.urls import path
from service_orders.views import ServiceOrderListView, ServiceOrderCreateView


urlpatterns = [
    path('service_orders/', ServiceOrderListView.as_view(), name='service_orders'),
    path('service_orders/create/', ServiceOrderCreateView.as_view(), name='service_orders_create'),
]
