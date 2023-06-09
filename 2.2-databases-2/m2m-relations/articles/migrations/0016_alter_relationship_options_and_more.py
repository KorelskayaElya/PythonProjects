# Generated by Django 4.2.2 on 2023-06-16 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_remove_object_relationships_object_scopes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relationship',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статей'},
        ),
        migrations.RenameField(
            model_name='relationship',
            old_name='object_main',
            new_name='is_main',
        ),
        migrations.RemoveField(
            model_name='object',
            name='scopes',
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='articles', through='articles.Relationship', to='articles.object'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_relationships', to='articles.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object_relationships', to='articles.object', verbose_name='Тег'),
        ),
    ]
