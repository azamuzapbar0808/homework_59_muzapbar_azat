# Generated by Django 4.1.6 on 2023-02-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_article_detailed_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='deleted_at',
            field=models.DateField(default=None, null=True, verbose_name='дата удаления'),
        ),
        migrations.AddField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='удалено'),
        ),
    ]