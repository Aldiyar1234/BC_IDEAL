from django.db import models


# Create your models here.
class Quiz(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    image = models.ImageField('Обложка')

    def __str__(self):
        return self.name


class Answer(models.Model):
    name = models.CharField('Ответ', max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField('Вопрос', max_length=255)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    points = models.PositiveIntegerField('Вес вопроса')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.name