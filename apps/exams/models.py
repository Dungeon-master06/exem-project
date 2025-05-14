from django.db import models
from ckeditor.fields import RichTextField


class Test(models.Model):
    title = models.CharField(verbose_name='Название теста', max_length=200)
    image = models.ImageField("Изображение", upload_to='tests/', blank=True, null=True)
    subject = models.CharField("Предмет", max_length=100)
    description = RichTextField("Описание", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(
        Test, verbose_name="Тест", 
        on_delete=models.CASCADE, related_name="questions"
    )
    text = RichTextField(verbose_name="Текст вопроса")

    class Meta:
        verbose_name = 'Вопрос теста'
        verbose_name_plural = 'Вопросы теста'
        ordering = ['id']
    
    def __str__(self):
        return f"Вопрос №{self.id}: {self.text[:50]}... Тема: {self.test.subject}"


class Answer(models.Model):
    question = models.ForeignKey(
        Question, verbose_name="Вопрос",
        on_delete=models.CASCADE, related_name="answers"
    )
    text = models.CharField(max_length=200, verbose_name="Текст ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ?")

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['question', 'id']
    
    def __str__(self):
        return f"Ответ: {self.text[:30]}... ({'✔' if self.is_correct else '❌'})"
