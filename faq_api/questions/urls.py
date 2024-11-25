from django.urls import path
from .views import FAQListView, FAQDetailView, FAQByTypeView, FAQByTypeAndCategoryView, FAQByTypeAndCategoryAndSubCategoryView

urlpatterns = [
    path('', FAQListView.as_view(), name='faq-list'),
    path('<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
    path('type:<slug:type_slug>/', FAQByTypeView.as_view(), name='faq-by-type'),
    path('type:<slug:type_slug>/category:<slug:category_slug>/', FAQByTypeAndCategoryView.as_view(), name='faq-by-type-and-category'),
    path('type:<slug:type_slug>/category:<slug:category_slug>/subcategory:<slug:subcategory_slug>/', FAQByTypeAndCategoryAndSubCategoryView.as_view(), name='faq-by-type-and-category-and-subcategory'),
]