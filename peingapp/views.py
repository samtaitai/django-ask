from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def index(request):
    questions = Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'peingapp/index.html', {'questions': questions.reverse()})

def new_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()
            return redirect('index',)
    else:
        form = QuestionForm()

    return render(request, 'peingapp/new_question.html', {'form': form})

def new_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = "admin"
            answer.save()
            return redirect('index',)
    else:
        form = AnswerForm()

    return render(request, 'peingapp/new_answer.html', {'form': form, 'question': question})


