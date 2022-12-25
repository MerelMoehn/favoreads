# Generated by Django 3.2.16 on 2022-12-25 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookcases', '0004_alter_book_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcase_book',
            name='bookcase_id',
        ),
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='book_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookcase_book',
            name='bookcase_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookcase_owner', to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Bookcase',
        ),
    ]