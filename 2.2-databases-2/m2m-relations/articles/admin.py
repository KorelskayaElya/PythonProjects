from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms

from .models import Tag, Relationship, Article


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'published_at', 'image']


class RelationshipInlineForm(forms.ModelForm):
    class Meta:
        model = Relationship
        exclude = []

    def clean(self):
        cleaned_data = super().clean()
        is_main = cleaned_data.get('is_main')
        article = cleaned_data.get('article')

        if is_main and Relationship.objects.filter(article=article, is_main=True).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Может быть только один основной тег для каждой статьи.')

        return cleaned_data


class RelationshipInline(admin.TabularInline):
    model = Relationship
    form = RelationshipInlineForm
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    inlines = [RelationshipInline]