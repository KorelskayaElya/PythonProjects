# Generated by Django 4.2.2 on 2023-06-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_remove_relationship_object_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='object_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
