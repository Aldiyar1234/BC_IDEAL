from itertools import groupby

from django.shortcuts import render
from quiz.models import Quiz, Question, Answer, University, UniversityRightFact, UniversityLeftFact, Major, Subject



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
    sorted_majors = sorted(majors, key=lambda x: (x.subject1.name, x.subject2.name))
    group_majors = groupby(sorted_majors, key=lambda x: (x.subject1.name, x.subject2.name))
    results = []
    for (subject1, subject2), group in group_majors:
        results.append([f"{subject1} и {subject2}", list(group)])
    return render(request, 'majors.html', {'majors': results, 'university':university})


def major_detail(request, university, pk):
    university = University.objects.get(url=university)
    major = Major.objects.get(pk=pk)
    return render(request, 'major.html', {'major': major, 'university': university})


def filters(request):
    majors = None
    subjects = Subject.objects.all()
    subject1 = request.GET.get('subject1')
    subject2 = request.GET.get('subject2')
    number = request.GET.get('number')
    if subject1 and subject2:
        majors = Major.objects.filter(subject1=subject1, subject2=subject2)
    if number:
        if majors :
            majors = majors.filter(minimum_grant_ball__lte=number)
        else:
            majors = Major.objects.filter(minimum_grant_ball__lte=number)
    return render(request, 'filters.html', {'subjects': subjects,'majors':majors, 'form':request.GET})
