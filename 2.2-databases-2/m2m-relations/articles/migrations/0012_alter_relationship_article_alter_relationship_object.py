# Generated by Django 4.2.2 on 2023-06-16 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_remove_article_relationships_object_relationships'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.article', verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.object', verbose_name='Раздел'),
        ),
    ]
