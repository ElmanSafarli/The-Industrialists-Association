from modeltranslation.translator import register, TranslationOptions
from .models import Company, IndustryCategory

@register(IndustryCategory)
class IndustryCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'location', 'country', 'industry', 'category')






