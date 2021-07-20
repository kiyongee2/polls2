from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    #return HttpResponse("안녕하세요! 설문조사 페이지입니다.")
    question_list = Question.objects.order_by('-pub_date')
    list = ', '.join([q.question_text for q in question_list])
    return HttpResponse(list)

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def vote(request,question_id):
    return HttpResponse("투표중입니다. %s." % question_id)