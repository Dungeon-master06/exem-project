from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название теста")
    subject = models.CharField(max_length=100, verbose_name="Предмет")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Тест"  # Название в единственном числе (админка)
        verbose_name_plural = "Тесты"  # Название во множественном числе
        ordering = ['title']  # Сортировка по названию (можно добавить `-created_at` если добавить поле даты)

    def __str__(self):
        return self.title
    


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions', verbose_name="Тест")
    text = models.TextField(verbose_name="Текст вопроса")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        ordering = ['id']  # Сортировка по порядку создания (можно заменить на `test` или другое поле)

    def __str__(self):
        return f"Вопрос #{self.id}: {self.text[:50]}..."  # Укороченное отображение


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name="Вопрос")
    text = models.CharField(max_length=200, verbose_name="Текст ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ?")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ['question', 'id']  # Сортировка сначала по вопросу, затем по ID

    def __str__(self):
        return f"Ответ: {self.text[:30]}... ({'✓' if self.is_correct else '✗'})"  # С пометкой правильности