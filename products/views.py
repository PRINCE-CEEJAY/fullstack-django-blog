from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, redirect, render
from products.models import Products

# CLASS BASED VIEW
class ProductsView(LoginRequiredMixin, TemplateView):
    login_url = 'users:login'
    template_name = 'products/show_products.html'

    # get method format
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['products'] = Products.objects.all().order_by('-createdAt')
         return context
    
    # post method
    def post(self, request):
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        available = data.get('available') == 'on'

        if not all([name, description, price]):
            context = self.get_context_data()
            context['error'] = 'all fields are required'
            return self.render_to_response(context)

        if not price.isdigit():
            context = self.get_context_data()
            context['error'] = 'price must be a digit'
            return self.render_to_response(context)
        
        new_product = Products.objects.create(name=name, description=description, price=int(price), available=available)        
        new_product.save()

        return redirect('products:show_products')
