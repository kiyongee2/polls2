from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {'question_list': question_list}
    return render(request, 'poll/list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'poll/detail.html', context)

def vote(request,question_id):
    return HttpResponse("투표중입니다. %s." % question_id)