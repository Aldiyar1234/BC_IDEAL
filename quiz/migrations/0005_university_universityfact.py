# Generated by Django 4.2 on 2023-05-13 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_answer_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('href', models.CharField(max_length=255, verbose_name='Ссылка')),
                ('image', models.ImageField(upload_to='logo', verbose_name='Логотип')),
                ('url', models.SlugField(verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Факт')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.university')),
            ],
        ),
    ]
