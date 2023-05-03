from django.shortcuts import render
from quiz.models import Quiz, Question, Answer



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
            answers[question.answer] = 0

        for pk in request.POST:
            if pk.isdigit():
                if request.POST[pk] == "YES":
                    question = questions.get(pk=pk)
                    answers[question.answer] += question.points

        if sum(answers.values()) == 0:
            results = [{'name': 'Не знаем!','description':'Чтобы мы смогли определить подходящую профессию для вас вам нужно ответить "ДА" хотя бы на один вопрос!!!'}]
        else:
            result = max(answers, key = answers.get)
            points = answers[result]
            results = []
            for answer in answers:
                if answers[answer] == points:
                    results.append(answer)
        print(results)
        return render(request, 'results.html', {'results': results})

    return render(request, 'questions.html', {'questions': questions, 'quiz': quiz})