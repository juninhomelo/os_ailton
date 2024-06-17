from django.urls import path
from services.views import ServiceListView, ServiceCreateView, ServiceDetailView, ServiceUpdateView, ServiceDeleteView


urlpatterns = [
    path('services/', ServiceListView.as_view(), name='services'),
    path('services/create/', ServiceCreateView.as_view(), name='services_create'),
    path('services/<int:pk>/detail', ServiceDetailView.as_view(), name='services_detail'),
    path('services/<int:pk>/update', ServiceUpdateView.as_view(), name='services_update'),
    path('services/<int:pk>/delete', ServiceDeleteView.as_view(), name='services_delete'),
]