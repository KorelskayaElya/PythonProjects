# Generated by Django 4.2.2 on 2023-06-16 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_alter_relationship_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Object',
            new_name='Tag',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='object',
        ),
        migrations.AddField(
            model_name='relationship',
            name='tag',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tag_relationships', to='articles.tag', verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_relationships', to='articles.article', verbose_name='Статья'),
        ),
    ]
