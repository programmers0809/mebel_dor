from django.shortcuts import render

from django.views import View

from .models import ProductModel


class HomeView(View):
    def get(self, request):
        products_list = ProductModel.objects.all()
        
        context = {
            'products_list' : products_list
        }
        return render(request, 'home.html', context=context)
    
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class CategoryView(View):
    def get(self, request):
        return render(request, 'category.html')
    
class ProductView(View):
    def get(self, request):
        return render(request, 'productpage.html')
    
class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')
