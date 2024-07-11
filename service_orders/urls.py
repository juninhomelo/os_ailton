from django.urls import path
from service_orders.views import ServiceOrderListView, ServiceOrderCreateView, ServiceOrderDetailView, ServiceOrderUpdateView, ServiceOrderDeleteView, generate_pdf, BrandCreateView


urlpatterns = [
    path('service_orders/', ServiceOrderListView.as_view(), name='service_orders'),
    path('service_orders/create/', ServiceOrderCreateView.as_view(), name='service_orders_create'),
    path('service_orders/<int:pk>/detail/', ServiceOrderDetailView.as_view(), name='service_orders_detail'),
    path('service_orders/<int:pk>/update/', ServiceOrderUpdateView.as_view(), name='service_orders_update'),
    path('service_orders/<int:pk>/delete/', ServiceOrderDeleteView.as_view(), name='service_orders_delete'),
    path('generate_pdf/<int:pk>/', generate_pdf, name='generate_pdf'),
    path('service_orders/brand/create/', BrandCreateView.as_view(), name='brand_create'),
    path('service_orders/brand/', BrandCreateView.as_view(), name='brands'),
]
