from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('play_turn/', play_turn.as_view()),
]