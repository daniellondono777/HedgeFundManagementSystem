# Generated by Django 4.0.8 on 2022-10-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hfma_app', '0003_controlpanel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlpanel',
            name='name',
            field=models.TextField(default='ControlPanel.:21-10-2022', max_length=30),
        ),
    ]
