from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Brand, Store
from .forms import AddBrandForm, AddStoreForm
from django.shortcuts import get_object_or_404
from .serializers import BrandSerializer, StoreSerializer, CreateStoreSerializer


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


@csrf_exempt
def api_list_brands(request):
    if request.method == 'GET':
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BrandSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)


@csrf_exempt
def api_details_brands(request, id):
    try:
        brand = Brand.objects.get(pk=id)
    except Brand.DoesNotExist:
        return JsonResponse({'message': 'Brands Do not exists'}, status=404)

    if request.method == 'DELETE':
        brand.delete()
        return JsonResponse({'message': 'Brand Has been deleted'}, status=200)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BrandSerializer(brand, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Brand Has been Updated'}, status=200)
        return JsonResponse({'message': 'Eroor whiling updating Brand'}, status=400)


@csrf_exempt
def api_store(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreateStoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'data not valide creating store'}, safe=False)


@csrf_exempt
def api_store_detail(request, id):
    try:
        store = Store.objects.get(pk=id)
    except Store.DoesNotExist:
        return JsonResponse({'message': 'Store Do not exists'}, status=404)

    if request.method == 'DELETE':
        store.delete()
        return JsonResponse({'message': 'Store Has been deleted'}, status=200)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CreateStoreSerializer(store, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Brand Has been Updated'}, status=200)
        else:
            return JsonResponse({'message': 'Eroor whiling updating Store'}, status=400)
