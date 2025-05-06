from django.contrib import admin 
from .models import Test, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('text', 'test')
    list_filter = ('test',)


class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')
    search_fields = ('title', 'subject')
    list_filter = ('subject',)
    fields = ('title', 'subject', 'description', 'image')


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)