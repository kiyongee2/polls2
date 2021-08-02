from django.http import HttpResponse
from django.shortcuts import render

def input(request): # HttpRequest
    #return HttpResponse("입력 화면 입니다.")
    return render(request, 'calc/input.html')

def output(request):
    # 데이터 받아서 넘기기
    name = request.POST['name']
    age = int(request.POST['age'])

    context = {'name': name, 'age': age}
    return render(request, 'calc/output.html', context)

def input_num(request):
    return render(request, 'calc/input_num.html')

def even_odd(request):
    # 숫자 받아오기
    num = int(request.POST['num'])

    # 홀수/짝수 계산
    if num % 2 == 1:
        context = {'num': num, 'result' : "홀수입니다."}
    else:
        context = {'num': num, 'result' : "짝수입니다."}

    return render(request, 'calc/even_odd.html', context)

def input_dan(request):
    return render(request, 'calc/input_dan.html')


def gugudan(request):
    # dan 전송받기
    dan = int(request.POST['dan'])

    # 구구단 계산하기
    times = []   # dan = 4, times=[4, 8, 12...32, 36]
    for i in range(1, 10):
        times.append(dan * i)

    context = {'dan': dan, 'times': times}
    return render(request, 'calc/gugudan.html', context)