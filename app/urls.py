from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customers.urls')),
    path('', include('products.urls')),
    path('', include('services.urls')),
    path('', include('service_orders.urls')),
]
