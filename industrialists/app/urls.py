from django.urls import path
from .views import HomePage, AllCompaniesView, CompanyDetailView, CategoryCompaniesView, AllCategoriesView, AboutUs

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('team/', AboutUs.as_view(), name='team'),
    path('companies/', AllCompaniesView.as_view(), name='all_companies'),
    path('categories/', AllCategoriesView.as_view(), name='all_categories'),
    path('<str:company_name>/', CompanyDetailView.as_view(), name='company_detail'),
    path('category/<str:category_name>/', CategoryCompaniesView.as_view(), name='category_companies'),
]
