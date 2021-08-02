from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    # /poll/
    path("", views.index, name='index'),
    # /poll/2
    path("<int:question_id>/", views.detail, name='detail'),
    # /poll/2/vote
    path("<int:question_id>/vote/", views.vote, name='vote'),

    path("<int:question_id>/results/", views.results, name='results'),


    # /poll/val_jq
    path("val_jq/", views.val_jq, name='val_jq'),
    path("parent_jq/", views.parent_jq, name='parent_jq'),
    path("submenu/", views.submenu, name="submenu"),
]