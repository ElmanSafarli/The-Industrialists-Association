from django.contrib import admin
from .models import Company, IndustryCategory, SubCategory
from modeltranslation.admin import TranslationAdmin


@admin.register(Company)
class CompanyAdmin(TranslationAdmin):
    list_display = ('name', 'creation_date', 'industry', 'country')
    search_fields = ('name', 'industry', 'country')
    list_filter = ('industry', 'country')

@admin.register(IndustryCategory)
class IndustryCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'background_image')
    search_fields = ('name',)

@admin.register(SubCategory)
class IndustrySubCategoryAdmin(TranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)