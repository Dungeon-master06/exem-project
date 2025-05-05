from django.shortcuts import render, get_object_or_404
from .models import Test, Question, Answer


def test_list(request):
    # Список всех тестов для учеников
    tests = Test.objects.all()
    context = {
        'tests':tests,
    }
    return render(request, 'exams/test_list.html', context)

def take_test(request, test_id):
    # Страница для прохождения теста
    test = get_object_or_404(Test, id=test_id)
    
    if request.method == 'POST':
        # подсчет баллов
        score = 0 
        for question in test.questions.all():
            selected_answer_id = request.POST.get(f'q_{question.id}')
            if selected_answer_id:
                if Answer.objects.get(id=selected_answer_id).is_correct:
                    score+=1
        context = {
            'test':test,
            'score':score,
            'total':test.questions.count(),
        }
        return render(request, 'exams/test_result.html', context)
    context = {
        'test':test
    }
    return render(request, 'exams/take_test.html', context)