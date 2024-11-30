from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ, Type, Category, SubCategory
from .serializers import FAQSerializer


class FAQListView(APIView):
    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True, context={'request': request})
        return Response(serializer.data)


class FAQDetailView(APIView):
    def get(self, request, pk):
        faq = get_object_or_404(FAQ, pk=pk)
        serializer = FAQSerializer(faq, context={'request': request})
        return Response(serializer.data)


class FAQByTypeView(APIView):
    def get(self, request, type_slug):
        faqs = FAQ.objects.filter(type__slug=type_slug)
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

class FAQByTypeAndCategoryView(APIView):
    def get(self, request, type_slug, category_slug):
        faqs = FAQ.objects.filter(type__slug=type_slug, category__slug=category_slug)
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

class FAQByTypeAndCategoryAndSubCategoryView(APIView):
    def get(self, request, type_slug, category_slug, subcategory_slug):
        faqs = FAQ.objects.filter(type__slug=type_slug, category__slug=category_slug, subcategory__slug=subcategory_slug)
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)

