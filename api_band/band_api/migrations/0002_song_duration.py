# Generated by Django 3.2.8 on 2021-10-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.FloatField(null=True),
        ),
    ]
