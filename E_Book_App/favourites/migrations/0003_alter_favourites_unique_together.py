# Generated by Django 5.1.2 on 2024-12-11 15:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_author_name'),
        ('favourites', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favourites',
            unique_together={('user', 'book')},
        ),
    ]
