# Generated by Django 4.0.8 on 2022-11-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hfma_app', '0007_remove_asset_financial_indicators_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='financial_indicators',
            field=models.JSONField(default='default'),
            preserve_default=False,
        ),
    ]
