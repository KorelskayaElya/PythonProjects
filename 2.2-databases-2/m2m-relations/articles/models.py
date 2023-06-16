from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField('Tag', through='Relationship', related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='relationships',
                                verbose_name='Статья')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='relationships', verbose_name='Тег',
                            default=None)
    is_main = models.BooleanField(default=False, verbose_name="Основной")

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статей'

    def __str__(self):
        return f'{self.article.title} - {self.tag.name} ({self.is_main})'