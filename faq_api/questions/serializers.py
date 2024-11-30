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
    class Meta:
        model = FAQ
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Преобразуем URL изображений, если они заданы
        if representation.get('question_image'):
            # Заменяем URL для question_image на относительный
            representation['question_image'] = representation['question_image'].replace('/media/', '/api/media/')

        if representation.get('answer_image'):
            # Заменяем URL для answer_image на относительный
            representation['answer_image'] = representation['answer_image'].replace('/media/', '/api/media/')

        return representation