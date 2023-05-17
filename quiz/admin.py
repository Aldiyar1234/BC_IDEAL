from django.contrib import admin
from quiz.models import Quiz, Question, Answer, University, UniversityLeftFact, UniversityRightFact, UniversityCategory, Major


class QuestionAdmin(admin.StackedInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionAdmin]

class UniversityLeftFactAdmin(admin.StackedInline):
    model = UniversityLeftFact

class UniversityRightFactAdmin(admin.StackedInline):
    model = UniversityRightFact

class UniversityMajorAdmin(admin.StackedInline):
    model = Major


class UniversityAdmin(admin.ModelAdmin):
    inlines = [UniversityLeftFactAdmin, UniversityRightFactAdmin, UniversityMajorAdmin]


# Register your models here.
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer)
admin.site.register(University,UniversityAdmin)
admin.site.register(UniversityCategory)


