# Generated by Django 3.2.16 on 2023-01-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcases', '0010_book_submitted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='excerpt',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]