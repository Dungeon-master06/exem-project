from django.db import models
from ckeditor.fields import RichTextField

class Settings(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название сайта")
    logo = models.ImageField(upload_to='images', verbose_name="Лого")
    phone1 = models.CharField(
        max_length=20, verbose_name="Телефон",
        help_text="Вы можете начать номер телефона с +996 (700) 700 700")
    email = models.CharField(max_length=100, verbose_name="E-mail")
    address = models.CharField(max_length=255, verbose_name="Адрес",null=True)
    map = models.TextField(verbose_name="карта", null=True)

    def __str__(self):
        return f"{self.name} {self.phone1}"

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'