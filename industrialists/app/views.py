from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Company, IndustryCategory
from django.db.models import Q

class HomePage(TemplateView):
    template_name = 'pages/home.html'


class AllCompaniesView(TemplateView):
    template_name = 'pages/all_companies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve all companies
        companies = Company.objects.all()

        # Get unique values for countries and industries
        unique_countries = companies.values_list('country', flat=True).distinct()
        unique_industries = companies.values_list('industry', flat=True).distinct()

        # Get filters from query parameters
        country_filter = self.request.GET.get('country')
        industry_filter = self.request.GET.get('industry')
        search_query = self.request.GET.get('q')

        # Apply filters
        if country_filter:
            companies = companies.filter(country=country_filter)
        if industry_filter:
            companies = companies.filter(industry=industry_filter)

        # Apply search filter for both name and category
        if search_query:
            companies = companies.filter(
                Q(name__icontains=search_query) | Q(industry__icontains=search_query)
            )

        # Apply sorting
        sort_by = self.request.GET.get('sort_by')
        if sort_by:
            companies = companies.order_by(sort_by)

        context['companies'] = companies
        context['unique_countries'] = unique_countries
        context['unique_industries'] = unique_industries
        context['search_query'] = search_query
        return context

class CompanyDetailView(TemplateView):
    template_name = 'pages/company_detail.html'

    def get_context_data(self, company_name, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = get_object_or_404(Company, name=company_name)

        # Retrieve the 5 most recently added companies
        context['recent_companies'] = Company.objects.order_by('-creation_date')[:5]

        return context

class CategoryCompaniesView(TemplateView):
    template_name = 'pages/category_companies.html'

    def get_context_data(self, category_name, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(IndustryCategory, name=category_name)
        companies = Company.objects.filter(category=category)
        context['category'] = category
        context['companies'] = companies

        # Get unique values for countries
        unique_countries = companies.values_list('country', flat=True).distinct()
        context['unique_countries'] = unique_countries

        # Check if search is made from a category page
        if 'q' in self.request.GET:
            search_query = self.request.GET.get('q')

            # If search is made from a category page, search only by the company name in that category
            context['search_category'] = True
            context['search_query'] = search_query
            companies = companies.filter(name__icontains=search_query)
            context['companies'] = companies

        # Get all categories for displaying in the template
        all_categories = IndustryCategory.objects.all()
        context['all_categories'] = all_categories

        return context

    def get_redirect_url(self):
        category_name = self.kwargs.get('category_name')
        country_name = self.request.GET.get('country')
        redirect_url = f'/category/{category_name}/'
        if country_name:
            redirect_url += f'?country={country_name}'
        return redirect_url

    def get(self, request, *args, **kwargs):
        # If both category and country are specified, redirect to the filtered URL
        if 'country' in request.GET and 'category_name' in kwargs:
            return redirect(self.get_redirect_url())

        return super().get(request, *args, **kwargs)

class AllCategoriesView(TemplateView):
    template_name = 'pages/all_categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_categories = IndustryCategory.objects.all()
        context['all_categories'] = all_categories
        return context