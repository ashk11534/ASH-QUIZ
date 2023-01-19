from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class ExamCategory(models.Model):

    name = models.CharField(max_length=100)

    slug = models.SlugField(max_length=150, unique=True, null=True)

    image = models.ImageField(upload_to='category_images/')

    class Meta:

        verbose_name_plural = 'ExamCategories'

    def __str__(self):

        return self.name


class Exam(models.Model):

    name = models.CharField(max_length=300)

    slug = models.SlugField(max_length=400, unique=True, null=True)

    category = models.ForeignKey(ExamCategory, on_delete=models.CASCADE)

    participants = models.ManyToManyField(User, blank=True)

    def __str__(self):

        return self.name


class Question(models.Model):

    title = models.CharField(max_length=400)

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):

        return f'Question - #{self.id}({self.title})'


class Option(models.Model):

    title = models.CharField(max_length=300)

    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)

    def __str__(self):

        return f'Option - #{self.id}({self.title}) - ({self.question.title})'


class CorrectAnswer(models.Model):

    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)

    def __str__(self):

        return f'Correct answer - #{self.option}'

class SubmittedAnswer(models.Model):

    submitted_answers = models.TextField(max_length=10000)

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True)

    number_of_correct_answers = models.PositiveBigIntegerField(null=True)

    submit_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return f'Submitted answer - #{self.id}'

