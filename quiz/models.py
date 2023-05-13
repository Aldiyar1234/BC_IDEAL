from django.db import models


class Quiz(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    image = models.ImageField('Обложка')

    def __str__(self):
        return self.name


class Answer(models.Model):
    name = models.CharField('Ответ', max_length=255)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField('Вопрос', max_length=255)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    points = models.PositiveIntegerField('Вес вопроса')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField('Название', max_length=255)
    href = models.CharField('Ссылка на университет', max_length=255)
    image = models.ImageField('Логотип', upload_to="logo")
    url = models.SlugField('Ссылка')
    fact = models.CharField('Факт', blank=True, max_length=255)
    abb = models.CharField('Аббревиатура', blank=True, max_length=255)

    def __str__(self):
        return self.name


class UniversityLeftFact(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField('Факт', max_length=255)

    def __str__(self):
        return self.name


class UniversityRightFact(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField('Факт', max_length=255)

    def __str__(self):
        return self.name
