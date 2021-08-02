from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {'question_list': question_list}
    return render(request, 'poll/list.html', context)

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'poll/detail.html', context)

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:

        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': '선택을 해주세요!'
        })
    else:
        selected_choice.votes += 1    #선택 하면 1이 증가함
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'poll/results.html', context)

def val_jq(request):
    return render(request, 'poll/val_jq.html')

def parent_jq(request):
    return render(request, 'poll/parent_jq.html')

def submenu(request):
    return render(request, 'poll/submenu.html')
