from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Brand, Store
from .forms import AddBrandForm, AddStoreForm
from django.shortcuts import get_object_or_404


# Create your views here.
def list_brands(request):
    if request.method == 'POST':
        data = AddBrandForm(request.POST)
        if data.is_valid():
            b = Brand.objects.create(name=data.data.get('name'))
            b.save()
    brands = Brand.objects.all()
    return render(request, 'brand/view.html', context={"brands": brands})


def delete_brand(request, id):
    brand = get_object_or_404(Brand, id=id)
    brand.delete()
    return redirect('brands')


def update_brand(request, id):
    brand = get_object_or_404(Brand, id=id)
    if request.method == 'POST':
        data = AddBrandForm(request.POST)
        if data.is_valid():
            brand.name = data.data.get('name')
            brand.save()
            return redirect('brands')
    return render(request, 'brand/edit.html', context={'brand': brand})


def list_stores(request):
    if request.method == 'POST':
        data = AddStoreForm(request.POST)
        if data.is_valid():
            s = Store.objects.create(name=data.data.get('name'), brand_id=data.data.get('brand'))
            s.save()
    brands = Brand.objects.all()
    stores = Store.objects.all()
    return render(request, 'store/view.html', context={
        'stores': stores,
        'brands': brands
    })


def delete_store(request, id):
    store = get_object_or_404(Store, id=id)
    store.delete()
    return redirect('list_stores')


def update_store(request, id):
    store = get_object_or_404(Store, id=id)
    brands = Brand.objects.all()
    if request.method == 'POST':
        data = AddStoreForm(request.POST)
        if data.is_valid():
            store.name = data.data.get('name')
            store.brand_id = data.data.get('brand')
            store.save()
            return redirect('list_stores')
    return render(request, 'store/edit.html', context={'store': store, 'brands': brands})
