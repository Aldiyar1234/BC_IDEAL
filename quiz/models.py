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


class UniversityCategory(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField('Название', max_length=255)
    href = models.CharField('Ссылка на университет', max_length=255)
    image = models.ImageField('Логотип', upload_to="logo")
    url = models.SlugField('Ссылка')
    fact = models.CharField('Факт', blank=True, max_length=255)
    abb = models.CharField('Аббревиатура', blank=True, max_length=255)
    category = models.ForeignKey(UniversityCategory , on_delete=models.CASCADE, blank=True, null=True)
    amount_of_students = models.PositiveIntegerField('Количество студентов', blank=True)

    class Meta:
        ordering = ["name"]

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


class Subject(models.Model):
    name = models.CharField('Названиие предмета', max_length=255)

    def __str__(self):
        return self.name


class Major(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField('Название специальности', max_length=255)
    code = models.CharField('Код', max_length=255)
    minimum_ball = models.PositiveSmallIntegerField('Пороговый балл')
    minimum_grant_ball = models.PositiveSmallIntegerField('Минимальный балл')
    maximum_ball = models.PositiveSmallIntegerField('Максимальный балл')
    avg_ball = models.PositiveSmallIntegerField('Средний балл')
    amount_of_grants = models.PositiveSmallIntegerField('Количество грантов')
    subject1 = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True, related_name='subject1')
    subject2 = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True, related_name='subject2')

    def __str__(self):
        return self.name