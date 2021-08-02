from django.urls import path
from calc import views

app_name = 'calc'

urlpatterns = [
    # 입 출력
    path('input/', views.input, name='input'),
    path('output/', views.output, name='output'),

    # 홀수/짝수 판별
    path('input_num/', views.input_num, name='input_num'),
    path('even_odd/', views.even_odd, name='even_odd'),

    # 구구단 계산
    path('input_dan/', views.input_dan, name='input_dan'),
    path('gugudan/', views.gugudan, name='gugudan')
]