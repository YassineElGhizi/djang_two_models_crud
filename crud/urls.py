from django.urls import path
from .views import list_brands, delete_brand, update_brand, list_stores, delete_store, update_store, api_list_brands, \
    api_details_brands, api_store , api_store_detail

urlpatterns = [
    path('', list_brands, name='brands'),
    path('<int:id>/delete', delete_brand, name='delete_brand'),
    path('<int:id>/update', update_brand, name='update_brand'),
    path('stores/', list_stores, name='list_stores'),
    path('stores/<int:id>/delete', delete_store, name='delete_store'),
    path('stores/<int:id>/update', update_store, name='update_store'),
    path('brands', api_list_brands, name='api_brands'),
    path('brands/<int:id>/', api_details_brands, name='api_details_brands'),
    path('stores_api/', api_store),
    path('stores_api/<int:id>/', api_store_detail),
]
