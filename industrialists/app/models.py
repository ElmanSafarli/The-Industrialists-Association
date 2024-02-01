# models.py
from django.db import models
from django.utils.translation import gettext as _

class IndustryCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))
    background_image = models.ImageField(upload_to='category_images/', blank=True, null=True, verbose_name=_('Image'))

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    category = models.ForeignKey(IndustryCategory, on_delete=models.CASCADE, verbose_name=_('Category'))

    def __str__(self):
        return self.name

class Company(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Subcategory'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    creation_date = models.DateField(verbose_name=_('Creation Date'))
    image = models.ImageField(upload_to='company_images/', verbose_name=_('Image'))
    description = models.TextField(verbose_name=_('Description'))
    location = models.TextField(verbose_name=_('Location'))
    phone = models.CharField(max_length=20, verbose_name=_('Phone'))
    email = models.EmailField(verbose_name=_('Email'))
    instagram_link = models.URLField(blank=True, verbose_name=_('Instagram Link'))
    instagram = models.CharField(max_length=20, blank=True, verbose_name=_('Instagram'))
    viber = models.CharField(max_length=20, blank=True, verbose_name=_('Viber'))
    telegram = models.CharField(max_length=20, blank=True, verbose_name=_('Telegram'))
    map_embed_code = models.TextField(verbose_name=_('Map Embed Code'))
    industry = models.CharField(max_length=100, verbose_name=_('Industry'))
    country = models.CharField(max_length=100, verbose_name=_('Country'))
    category = models.ForeignKey(IndustryCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Category'))

    def __str__(self):
        return self.name
