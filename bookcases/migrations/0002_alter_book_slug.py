# Generated by Django 3.2.16 on 2022-12-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=1000, unique=True),
        ),
    ]