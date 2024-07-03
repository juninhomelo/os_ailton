from django.urls import path
from service_orders.views import ServiceOrderListView, ServiceOrderCreateView, ServiceOrderDetailView, ServiceOrderUpdateView, ServiceOrderDeleteView


urlpatterns = [
    path('service_orders/', ServiceOrderListView.as_view(), name='service_orders'),
    path('service_orders/create/', ServiceOrderCreateView.as_view(), name='service_orders_create'),
    path('service_orders/<int:pk>/detail/', ServiceOrderDetailView.as_view(), name='service_orders_detail'),
    path('service_orders/<int:pk>/update/', ServiceOrderUpdateView.as_view(), name='service_orders_update'),
    path('service_orders/<int:pk>/delete/', ServiceOrderDeleteView.as_view(), name='service_orders_delete'),
]
