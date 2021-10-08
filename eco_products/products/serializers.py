from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField

from .models import Category, Product


class CategorySerializer(ModelSerializer):
    """This serializer for Category-model"""

    products = StringRelatedField(many=True, read_only = True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'products']

class ProductSerializer(ModelSerializer):
    """This serializer for Category-model"""

    class Meta:
        model = Product
        fields = "__all__"
    def to_representation(self, instance):
        rep = super(ProductSerializer, self).to_representation(instance)
        rep['category'] = instance.category.name
        return rep   