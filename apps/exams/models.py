from django.db import models


class Test(models.Model):
    title = models.CharField(verbose_name='Название теста', max_length=200)
    subject = models.CharField("Предмет", max_length=100)
    description = models.TextField("Описание", blank=True, null=True)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['title']
    
    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(
        Test, verbose_name="Тест", 
        on_delete=models.CASCADE, related_name="questions"
    )
    text = models.TextField(verbose_name="Текст вопроса")

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
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
        return f"Ответ: {self.text[:30]}... ({'✅' if self.is_correct else '❎'})"
