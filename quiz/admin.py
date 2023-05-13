from django.contrib import admin
from quiz.models import Quiz, Question, Answer, University, UniversityLeftFact, UniversityRightFact


class QuestionAdmin(admin.StackedInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionAdmin]

class UniversityLeftFactAdmin(admin.StackedInline):
    model = UniversityLeftFact

class UniversityRightFactAdmin(admin.StackedInline):
    model = UniversityRightFact


class UniversityAdmin(admin.ModelAdmin):
    inlines = [UniversityLeftFactAdmin, UniversityRightFactAdmin]


# Register your models here.
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer)
admin.site.register(University,UniversityAdmin)


