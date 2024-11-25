# questions/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer
from django.shortcuts import get_object_or_404

class FAQListView(APIView):
    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

class FAQDetailView(APIView):
    def get(self, request, pk):
        faq = get_object_or_404(FAQ, pk=pk)
        serializer = FAQSerializer(faq)
        return Response(serializer.data)

class FAQByTypeView(APIView):
    def get(self, request, type_name):
        faqs = FAQ.objects.filter(type__name=type_name)
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

class FAQByTypeAndCategoryView(APIView):
    def get(self, request, type_name, category_name):
        faqs = FAQ.objects.filter(type__name=type_name, category__name=category_name)
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

class FAQByTypeAndCategoryAndSubCategoryView(APIView):
    def get(self, request, type_name, category_name, subcategory_name):
        faqs = FAQ.objects.filter(type__name=type_name, category__name=category_name, sub_category__name=subcategory_name)
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)