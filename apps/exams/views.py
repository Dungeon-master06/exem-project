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
    paginator = Paginator(tests, 6)
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
    # Страница для прохождения теста
    test = get_object_or_404(Test, id=test_id)
    settings = Settings.objects.order_by('-id').first()
    social_links = SocialLink.objects.all()
    
    if request.method == 'POST':
        # подсчет баллов
        score = 0 
        for question in test.questions.all():
            selected_answer_id = request.POST.get(f'q_{question.id}')
            if selected_answer_id:
                if Answer.objects.get(id=selected_answer_id).is_correct:
                    score+=1
        total = test.questions.count()
        recommend_books = []
        if score < total:
            recommend_books = Book.objects.filter(
                title__icontains=test.subject
            ).distinct()[:5]
        context = {
            'test':test,
            'score':score,
            'total': total,
            'recommend_books': recommend_books,
            'settings':settings,
            'social_links':social_links
        }
        return render(request, 'pages/exams/test_result.html', context)
    context = {
        'test':test,
        'settings':settings,
        'social_links':social_links
    }
    return render(request, 'pages/exams/take_test.html', context)