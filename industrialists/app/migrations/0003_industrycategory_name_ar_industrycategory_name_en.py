# Generated by Django 5.0.1 on 2024-01-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_industrycategory_background_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='industrycategory',
            name='name_ar',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='industrycategory',
            name='name_en',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Name'),
        ),
    ]
