# Generated by Django 4.2 on 2023-04-29 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ответ')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.PositiveIntegerField(default=1, verbose_name='Вес вопроса'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.answer'),
        ),
    ]
