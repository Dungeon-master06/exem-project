from django.contrib import admin 
from .models import Test, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')
    search_fields = ('title', 'subject')


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)