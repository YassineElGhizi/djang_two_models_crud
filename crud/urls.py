from django.urls import path
from .views import list_brands, delete_brand, update_brand, list_stores, delete_store , update_store

urlpatterns = [
    path('', list_brands, name='brands'),
    path('<int:id>/delete', delete_brand, name='delete_brand'),
    path('<int:id>/update', update_brand, name='update_brand'),
    path('stores/', list_stores, name='list_stores'),
    path('stores/<int:id>/delete', delete_store, name='delete_store'),
    path('stores/<int:id>/update', update_store, name='update_store'),

]
