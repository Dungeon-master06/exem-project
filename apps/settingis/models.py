from django.db import models
from ckeditor.fields import RichTextField


class Settings(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название сайта")
    logo = models.ImageField(upload_to='logo/', verbose_name="Лого")
    phone = models.CharField(
        max_length=20, verbose_name="Телефон",
        help_text="Вы можете начать номер телефона с +996 (700) 700 700")
    email = models.CharField(max_length=100, verbose_name="E-mail")
    address = models.CharField(max_length=255, verbose_name="Адрес",null=True)
    map = models.TextField(verbose_name="карта", null=True)

    def __str__(self):
        return f"{self.name} {self.phone}"

    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'


class FAQ(models.Model):
    question = models.CharField("Вопрос", max_length=255)
    answer = RichTextField("Ответ",config_name='default')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'


class SocialLink(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    url = models.URLField(verbose_name="Ссылка")
    icon = models.CharField(max_length=100, help_text='CSS-класс иконки Bootstrap, пример: bi bi-twitter, bi bi-instagram', verbose_name="Иконка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'