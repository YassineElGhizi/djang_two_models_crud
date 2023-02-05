from rest_framework import serializers
import serializer as serializer

from .models import Brand, Store


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class StoreSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = Store
        fields = ['id','name', 'brand']


class CreateStoreSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    brand_id = serializers.IntegerField(required=True)

    class Meta:
        model = Store
        fields = ['name', 'brand_id', 'brand']
