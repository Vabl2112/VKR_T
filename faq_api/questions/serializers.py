from rest_framework import serializers

from .models import Type, Category, SubCategory, FAQ


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    category = CategorySerializer()
    sub_category = SubCategorySerializer()

    class Meta:
        model = FAQ
        fields = '__all__'