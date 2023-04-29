from django.shortcuts import render
from quiz.models import Quiz, Question, Answer

# Create your views here.
def quizez(request):
    print('Кто-то посетил страницу')
    tests = Quiz.objects.all()
    return render(request, 'second_page.html', {'tests': tests, 'number': 5})


def questions(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == "POST":
        answers = {}
        for question in questions:
            answers[question.answer.name] = 0

        for pk in request.POST:
            if pk.isdigit():
                if request.POST[pk] == "YES":
                    question = questions.get(pk=pk)
                    answers[question.answer.name] += question.points

        result = max(answers, key = answers.get)

        return render(request, 'results.html', {'result': result})

    return render(request, 'questions.html', {'questions': questions, 'quiz': quiz})