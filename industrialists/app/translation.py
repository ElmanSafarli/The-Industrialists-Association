from modeltranslation.translator import register, TranslationOptions
from .models import Company, IndustryCategory, SubCategory

@register(IndustryCategory)
class IndustryCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'location', 'country', 'industry', 'category')






