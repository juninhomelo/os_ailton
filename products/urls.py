from django.urls import path
from products.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView


urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/detail/', ProductDetailView.as_view(), name='products_detail'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='products_delete'),
]
