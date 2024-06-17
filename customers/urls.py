from django.urls import path
from customers.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView

urlpatterns = [
    path('customers/', ClientListView.as_view(), name='customers'),
    path('customers/create/', ClientCreateView.as_view(), name='customers_create'),
    path('customers/<int:pk>/detail/', ClientDetailView.as_view(), name='customers_detail'),
    path('customers/<int:pk>/update/', ClientUpdateView.as_view(), name='customers_update'),
    path('customers/<int:pk>/delete/', ClientDeleteView.as_view(), name='customers_delete'),
]
