# Generated by Django 5.1.2 on 2024-12-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_author_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]