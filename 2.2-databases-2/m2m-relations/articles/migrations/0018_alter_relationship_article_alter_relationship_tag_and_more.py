# Generated by Django 4.2.2 on 2023-06-16 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_rename_object_tag_rename_title_tag_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='tag',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.tag', verbose_name='Тег'),
        ),
        migrations.AlterUniqueTogether(
            name='relationship',
            unique_together={('article', 'is_main')},
        ),
    ]
