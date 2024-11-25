from django.urls import path
from .views import (
    FAQListView,
    FAQDetailView,
    FAQByTypeView,
    FAQByTypeAndCategoryView,
    FAQByTypeAndCategoryAndSubCategoryView,
)

urlpatterns = [
    path('', FAQListView.as_view(), name='faq-list'),
    path('<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
    path('type/<str:type_name>/', FAQByTypeView.as_view(), name='faq-by-type'),
    path('type/<str:type_name>/category/<str:category_name>/', FAQByTypeAndCategoryView.as_view(), name='faq-by-type-and-category'),
    path('type/<str:type_name>/category/<str:category_name>/subcategory/<str:subcategory_name>/', FAQByTypeAndCategoryAndSubCategoryView.as_view(), name='faq-by-type-and-category-and-subcategory'),
]