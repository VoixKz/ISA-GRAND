# Generated by Django 5.1.3 on 2024-11-30 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_vacancymodel_is_hot'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
    ]