from django.contrib import admin

from .models import ExamCategory, Exam, Question, Option, CorrectAnswer, SubmittedAnswer

# Register your models here.

@admin.register(ExamCategory)
class ExamCategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Exam)
class Exam(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Question)

admin.site.register(Option)

admin.site.register(CorrectAnswer)

admin.site.register(SubmittedAnswer)
