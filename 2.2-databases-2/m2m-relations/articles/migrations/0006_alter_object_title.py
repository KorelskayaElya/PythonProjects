# Generated by Django 4.2.2 on 2023-06-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_relationship_delete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
    ]
