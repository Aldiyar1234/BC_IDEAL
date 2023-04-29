from django.contrib import admin
from quiz.models import Quiz, Question, Answer


class QuestionAdmin(admin.StackedInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionAdmin]


# Register your models here.
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer)
