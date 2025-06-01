from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Test, Answer
from apps.books.models import Book
from apps.settingis.models import Settings, SocialLink
from django.core.paginator import Paginator


def test_list(request):
    # Список всех тестов для учеников
    settings = Settings.objects.order_by('-id').first()
    social_links = SocialLink.objects.all()
    tests = Test.objects.all()
    search_query = request.GET.get('q', '')
    if search_query:
        tests = tests.filter(title__icontains=search_query)
    paginator = Paginator(tests, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = { 
        'settings':settings,
        'social_links':social_links,
        'tests': page_obj,
        'page_obj': page_obj,
        'recent_tests': Test.objects.order_by('-created_at')[:3],
        'total_tests': Test.objects.count()
    }
    return render(request, 'pages/exams/test_list.html', context)

@login_required(login_url='login')
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    settings = Settings.objects.order_by('-id').first()
    social_links = SocialLink.objects.all()
    questions = list(test.questions.all().order_by('id'))
    total_questions = len(questions)

    # Если нет вопросов — сразу вернуть шаблон с предупреждением
    if total_questions == 0:
        context = {
            'test': test,
            'question': None,
            'current_index': 0,
            'total_questions': 0,
            'settings': settings,
            'social_links': social_links,
        }
        return render(request, 'pages/exams/take_test.html', context)

    current_index = int(request.POST.get('current_index', 1))

    if request.method == 'POST':
        current_question = questions[current_index - 1]
        selected_answer_id = request.POST.get(f'q_{current_question.id}')
        if selected_answer_id:
            request.session[f'test_{test_id}_q_{current_question.id}'] = int(selected_answer_id)

        if current_index >= total_questions:
            score = 0
            for q in questions:
                ans_id = request.session.get(f'test_{test_id}_q_{q.id}')
                if ans_id and Answer.objects.filter(id=ans_id, is_correct=True).exists():
                    score += 1

            recommend_books = []
            if score < total_questions:
                recommend_books = Book.objects.filter(
                    title__icontains=test.subject
                ).distinct()[:5]

            for q in questions:
                request.session.pop(f'test_{test_id}_q_{q.id}', None)

            context = {
                'test': test,
                'score': score,
                'total': total_questions,
                'recommend_books': recommend_books,
                'settings': settings,
                'social_links': social_links,
            }
            return render(request, 'pages/exams/test_result.html', context)

        current_index += 1

    current_question = questions[current_index - 1]
    context = {
        'test': test,
        'question': current_question,
        'current_index': current_index,
        'total_questions': total_questions,
        'settings': settings,
        'social_links': social_links,
    }
    return render(request, 'pages/exams/take_test.html', context)
