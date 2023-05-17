from django.shortcuts import render
from quiz.models import Quiz, Question, Answer, University, UniversityRightFact, UniversityLeftFact, Major



def quizez(request):
    print('Кто-то посетил страницу')
    tests = Quiz.objects.all()
    return render(request, 'second_page.html', {'tests': tests})


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


def university_view(request, url):
    university = University.objects.get(url=url)
    university_left_facts = UniversityLeftFact.objects.filter(university=university)
    university_right_facts = UniversityRightFact.objects.filter(university=university)
    return render(request, 'university.html', {"university": university,"university_right_facts": university_right_facts, "university_left_facts": university_left_facts})


def homepage(request):
    universitys = University.objects.all()
    return render(request, 'index.html', {'universitys': universitys} )


def major_group(request, university):
    university = University.objects.get(url=university)
    majors = Major.objects.filter(university=university)
    return render(request, 'majors.html', {'majors': majors,'university':university})


def major_detail(request, university, pk):
    university = University.objects.get(url=university)
    major = Major.objects.get(pk=pk)
    return render(request, 'major.html', {'major': major, 'university': university})