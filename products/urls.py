from django.urls import path
from .views import ProductsView

app_name = 'products'

urlpatterns = [
    path('show_products/', ProductsView.as_view(), name='show_products')
]