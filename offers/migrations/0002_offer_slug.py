# Generated by Django 4.1.3 on 2022-11-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=160),
        ),
    ]
