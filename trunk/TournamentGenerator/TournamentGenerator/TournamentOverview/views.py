from django.shortcuts import render, get_object_or_404

from .forms import RawProductForm, ProductCreateForm
from .models import Products

# Create your views here.


def productCreateView(httprequest, *args, **kwargs):
    my_form = ProductCreateForm(httprequest.POST or None)

    if my_form.is_valid():
        my_form.save()        #Products.objects.create(**my_form.cleaned_data)
        my_form = ProductCreateForm()

    context = {
        "form" : my_form
    }

    return render(httprequest, "product_create_view.html", context)

"""
def productCreateView(httprequest, *args, **kwargs):
    my_form = RawProductForm(httprequest.POST or None)
    print(httprequest.POST)
    if my_form.is_valid():
        #print(**my_form.cleaned_data)
        Products.objects.create(**my_form.cleaned_data)
        my_form = RawProductForm()

    context ={
        "form" : my_form
    }

    return render(httprequest, "product_list.html", context)
"""

def productList(httprequest, *args, **kwargs):
    allProducts = Products.objects.all()
    context ={
        "allProducts" : allProducts,
        "title" : "My product list"
    }

    return render(httprequest, "product_list.html", context)


def productDetail(httprequest, my_id, *args, **kwargs):
    #oneProduct = Products.objects.get(id=my_id)
    oneProduct =get_object_or_404(Products, id=my_id)
    context ={
        "obj" : oneProduct,
        "title" : "Product Details"
    }

    return render(httprequest, "product_detail.html", context)
