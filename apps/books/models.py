from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = models.TextField(blank=True, verbose_name='Описание')
    file = models.FileField(upload_to='books/' , verbose_name="Файл")
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Обложка")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'