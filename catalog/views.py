from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView


# Create your views here.


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


#def contacts(request):
#    if request.method == "POST":
#        name = request.POST.get("name")
#phone = request.POST.get("phone")
##        message = request.POST.get("message")
#        print(f"{name} ({phone}): {message}")
#
#    return render(request, "contacts.html")


#def product_detail(request, pk):
#    product = get_object_or_404(Product, pk=pk)
 #   context = {"product": product}
#    return render(request, "product_detail.html", context)
