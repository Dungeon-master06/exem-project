from django.contrib import admin
from .models import Test, Question, Answer


class AnswerInline(admin.TabularInline):  # Или StackedInline для вертикального отображения
    model = Answer
    extra = 4  # Количество пустых полей для ответов

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]  # Добавляем ответы прямо в вопрос

class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')
    search_fields = ('title', 'subject')

admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
# Answer не регистрируем отдельно, т.к. он уже в QuestionAdmin через Inline