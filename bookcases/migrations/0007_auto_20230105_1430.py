# Generated by Django 3.2.16 on 2023-01-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcases', '0006_rename_book_id_bookcase_book_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='likes',
        ),
        migrations.AlterField(
            model_name='bookcase_book',
            name='status',
            field=models.IntegerField(choices=[(0, 'Not started'), (1, 'Reading'), (2, 'Read')], default=0),
        ),
    ]
