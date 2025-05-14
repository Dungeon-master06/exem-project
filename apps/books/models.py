from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категории книг'
        verbose_name_plural = 'Категории книг'


class Book(models.Model):
    category = models.ManyToManyField(Category, related_name='books', verbose_name="категория")
    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = RichTextField(blank=True, verbose_name='Описание')
    file = models.FileField(upload_to='books/' , verbose_name="Файл книги (.pdf)")
    cover_image = models.ImageField(upload_to='books/cover-image/', blank=True, null=True, verbose_name="Обложка книги")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    pages = models.PositiveBigIntegerField(validators=[MinValueValidator(100)], default=0, verbose_name="Количество страниц")
    year = models.PositiveIntegerField(validators=[MaxValueValidator(2025)],verbose_name="Год")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'