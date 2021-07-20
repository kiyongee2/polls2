from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    # /poll/
    path("", views.index),
    # /poll/2
    path("<int:question_id>/", views.detail, name='detail'),
    # /poll/2/vote
    path("<int:question_id>/vote/", views.vote, name='vote'),
]